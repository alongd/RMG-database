# I-221 — Metastable argon thermochemistry

Branch `i221-argon-metastable-thermo`, worktree
`/home/alon/Code/RMG-database-i221-argon-metastable-thermo`, cut from `plasma` at `04846619b`.
Engine `/home/alon/Code/RMG-Py-plasma` at `311818121`, conda env `rmg_env`. Every run below is
captured in `logs/` with both streams.

> **Merging this branch? Read [§19](#19-merge-requirement--this-branch-does-not-stand-alone)
> first.** This branch requires the RMG-Py branch `i221-saturation-no-atomtype`; on a pristine
> engine its suite is 322 passed and **2 failed by design** (measured on plasma head `98d465d3b`,
> round 90 — it was 1 until round 87 added the second negative control), and landing the two
> separately leaves the quarantine pin unenforced in the gap.

---

## 1. What was added

One new thermo library and one entry in it — plus, after round 58 and on the owner's ruling, one
quarantine manifest under `input/kinetics/` that refuses the rate this entry makes reachable
(§13.3). This section describes the entry as it stands *today*: it was a `ThermoData` until §13.4
replaced it with an algebraic `NASA`, and several numbers below moved by 0.0031 kJ/mol when it did.

| | |
|---|---|
| **Library** | `input/thermo/libraries/PlasmaExcitedNeutralThermo.py` |
| **Scope** | Gas-phase thermochemistry of electronically excited, electrically **neutral** species of plasma interest, each entry pinned to one named spectroscopic level |
| **Entry** | `Ar(3P2)` — `multiplicity 3 / 1 Ar u2 p3 c0` |
| **H298** | 1114.247 kJ/mol |
| **E0** | *not stated* — derived, 1108.0496 kJ/mol. See §10, HIGH-1 and §13.1 |
| **S298** | 168.227 J/(mol·K) |
| **Cp(T)** | 20.786 J/(mol·K) = 5/2·R, at every tabulated T |
| **Declared range** | 200 – 6000 K, and since §13.4 made it a `NASA` that is also what standard processing delivers. The 100 – 5000 K refit described in §10, HIGH-3 applied to the `ThermoData` form |

Plus `test/test_argon_metastable_thermo.py` (44 tests), `test/test_eii_quarantine.py` (14 tests),
and this directory.

Nothing else. Every path touched is inside `input/thermo/libraries/`, `test/`, `docs/` and — since
the ruling of 2026-09-15 — one added file under `input/kinetics/families/`. Measured against the
branch point `04846619b`, **every path is an addition: not one pre-existing tracked file is
modified**. Nothing pushed, nothing merged, no PR.

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

## 5. The three numbers, one identity each — and they are consistency checks, not corroboration

**Read this before the three.** An earlier version of this section presented "three numbers, one
identity each" as though three independent things had been checked. They are not independent, and
saying so costs nothing. `Cp`, `H` and `S` here are **construction identities**: `H` is the ASD
level energy times `h·c·N_A`, the eV cross-check below divides the *same* ASD energy by a unit
conversion, and `S` combines the *same* ASD level's `J` with JANAF's ground-state entropy. Each
identity confirms that the arithmetic that produced a number reproduces that number. None of them
tests the physics, and none of them would notice if the wrong ASD level had been transcribed —
only the level-identification work in §4 does that.

They are still worth having and are still pinned by tests, for what they actually are: they catch
transcription slips, unit errors and drift between the file and the report. The campaign withdrew
exactly this shape of claim three days ago on another ticket, where `1213 × 0.0085` was offered as
independent confirmation and was a first-order identity. Same correction, applied here before it
had to be pointed out twice.

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

**Form emitted: `NASA`, one polynomial over 200 – 6000 K.** The coefficients follow
*algebraically* from a constant Cp — `a1 = 5/2`, `a6 = H298/R − a1·298.15`, `a7 = S298/R −
a1·ln 298.15`, `a2..a5 ≡ 0` — so nothing is fitted and the charter is satisfied. It is what makes
the advertised 6000 K real: `process_thermo_data` keeps an already-`NASA` library entry verbatim
and refits anything else to a hard-coded 100 – 5000 K.

*Superseded, and left here as the record of what changed:* this entry was a `ThermoData` until
§13.4, justified on the ground that emitting a NASA would mean fitting. **That justification was
false** — see §13.4 for the retraction and for the four things the switch fixed. Wherever a section
below describes a `ThermoData`, it is describing the form before §13.4; the numbers that moved with
it are listed in §13.4 rather than restated in place.

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

**The 4 failures pre-date this work on the base it was cut from (`04846619b`) and are unrelated**,
identical before and after — engine-drift tripwires that fire because RMG-Py moved under them.
**They are NOT failures of the project**: they were already repaired at plasma head `96f2afa4a`,
and they go green here the moment this branch is rebasable onto it. See §16, which is the
correction; "pre-existing" below means *against this branch's base*, nowhere else:

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

4. **`Ar0e` in a *group* adjacency list does not mean "metastable" — but only at the group layer,
   and round 60 corrects this item.** Atom-type perception ignores `u` entirely, so the group
   `1 Ar0e ux p3 c0` compares equal to a u1 argon group as readily as to the u2 metastable, which
   is what RMG-Py's `atomtype.py` warns about at length. **No such molecule exists to be matched**,
   though: in a molecule the valency check applies, `8 - c = bonds + 2p + u` fixes `u`, and a
   bond-free neutral argon at p3 is u2 or it is refused. Measured over the whole (u, p, c) grid,
   exactly one molecule perceives as `Ar0e` and it is this species (§14.2). So the hazard is real
   for group-against-group comparison and unreachable in reaction generation, which matches groups
   against molecules. A group meaning this species should still write `u2`, for the reader.
   Also: the SMILES round trip is unsafe for monatomic species in this database
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
dH298(Ar -> Ar(3P2)) = 1114.2439 kJ/mol      against 1114.2468 exact   (-0.0029)
dS298(Ar -> Ar(3P2)) =   13.4922 J/(mol*K)   against   13.3816 exact   (+0.1106)
```

The enthalpy of excitation is low by 0.0029 kJ/mol; the entropy is 0.111 J/(mol·K) high, worth
−0.033 kJ/mol in ΔG at 298.15 K. **These are the numbers the entry as shipped delivers today**, and
they are not the ones this section carried until round 59 — see §13.4 for the superseded pair and
why both moved when the entry became a `NASA`. In one line: on the old form both sides carried the
same 298-vs-298.15 K field offset and it cancelled in each difference; a `NASA` has no such field,
so now the enthalpy residual is the winner's offset showing through and the entropy residual is
precedence measured on the API scale. Had one of the seven JANAF-agreeing libraries won instead,
the entropy residual would be ≈ −0.001 rather than +0.111.

**This hazard now has a detector**, which it did not before:
`test_the_anchor_error_the_engine_delivers_is_the_one_the_library_discloses` reads the pair above
out of the entry's own text and compares it with what the engine delivers with every library
loaded. It goes red when the file drifts from the measurement — which is exactly how the superseded
pair survived §13.4 — and when the resolved ground state changes. It does **not** close the hazard:
closing it means re-anchoring `BurkeH2O2` or giving RMG a way to require a ground-state anchor, and
both are other tickets. It makes it loud. The number is small; the *mechanism* is not, because nothing about it is
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
This entry *was* a `ThermoData` — chosen on charter grounds — so the declared ceiling was discarded.
(§13.4 replaced it with an algebraic `NASA` and the ceiling is now delivered; this paragraph records
the round-N finding that led there, not the state today.)

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

The round stated the admitted barrier as **406.334 kJ/mol**. Measured, it is **412.5234**.

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
| `[Ar]` E0 | 1108.0496 | **derived**, because this library states none |
| barrier actually applied | **412.5234** | the difference of those two |
| dHrxn(298) | 406.3371 | what both conventions agree on |
| leak | **6.1863** | exactly the cation library's stated-minus-derived gap |

**A correction to this section's own first draft, which quoted 1108.0527 / 412.5203 / 406.3340.**
Those were measured on the `ThermoData` form of this entry, before §13.4 replaced it with a `NASA`;
the probe log was not regenerated after the switch, so three numbers here described a version of
the entry that had already been superseded. Re-measured on the entry as shipped, each of the three
sits **+0.0031 kJ/mol** higher — that is 5/2·R·0.15, the 298-vs-298.15 K reference-temperature
offset that `ThermoData.to_wilhoit` carries and the NASA form does not. The **leak is identical to
four decimals under both forms**, because it belongs to `PlasmaCationThermo` and not to this
library; that invariance is what identifies it, and it is now asserted at `abs=1e-3` rather than the
original `abs=5e-3`, which was wide enough to straddle the move and keep passing on the stale value.
A tolerance larger than the effect under test is not a tolerance.

The round reported 412.5203 as an *Arkane-lookup* curiosity in the E0 residuals. It is not a
curiosity: **the mixed sibling convention sets the activation energy of the one reaction this
library makes reachable.** An Arrhenius barrier sits in an exponent, so the leak multiplies the
delivered rate by `exp(-6186.3/RT)` — 11.94× at 300 K, 2.10× at 1000 K.

This also reconciles the round's three rate numbers with mine exactly. Every one of the round's
values corresponds to a 406.334 barrier and every one of mine to 412.5234:

| T (K) | round | measured here | ratio | `exp(ΔEa/RT)` |
|---|---|---|---|---|
| 300 | 2.312e-63 | 1.933634e-64 | 11.9568 | 11.9577 |
| 1000 | 7.715e-14 | 3.664598e-14 | 2.1053 | 2.1052 |
| 34813.5 | 3.1764e7 | 3.109200e7 | 1.0216 | 1.0216 |

The round's qualitative conclusion is untouched and correct. The direction and the scale stand.

### 13.2 HIGH — the reachability disclosure, rewritten to the measured behaviour

Confirmed exactly as the round described. Ground-state argon generates zero reactions, the
metastable generates one, and `u0` versus `u2` is genuinely the discriminator. What happens next is
not what either the previous disclosure or the review question said:

```
delivered kf, T_gas =  300 K, Te = 1 eV   1.933634e-64 m^3/(mol*s)
delivered kf, T_gas =  300 K, Te = 3 eV   1.933634e-64      <- IDENTICAL
delivered kf, T_gas = 1000 K, Te = 1 eV   3.664598e-14
delivered kf, T_gas = 1000 K, Te = 3 eV   3.664598e-14      <- IDENTICAL
same Arrhenius evaluated at Te = 3 eV     3.109200e+07
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

### 13.3 The merge question — the quarantine, investigated, then written

**Yes, precisely. Investigated as directed, proposed, and — on the owner's ruling of 2026-09-15 —
written.** The manifest is
`input/kinetics/families/Plasma_Electron_Impact_Ionization/quarantine.py`; the gate is measured in
`quarantine_probe.py` (both streams in `logs/quarantine_probe.*.log`) and pinned by the 14 tests in
`test/test_eii_quarantine.py`. The investigation that led to it is kept below unchanged, because
the two refinements it produced are the reasons the manifest reads the way it does.

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

Manifest as proposed (the shipped file says the same and carries the measurement and the lift
conditions in full):

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

**What the gate does, measured** (`logs/quarantine_probe.stdout.log`):

* the manifest loads, resolves `KineticsModel` to the real class, and covers **1 of the family's 1
  rules**, computed from the loaded database rather than from a list;
* `apply_kinetics_to_reaction` on `Ar(3P2) => Ar+` raises `QuarantinedKineticsError`, naming the
  family, the rule (`A_rad`, rank 10), the kinetics class, the reason and the manifest path;
* the refused reaction is left **exactly as generated** — `reaction.kinetics` is still `None`, so
  nothing is half-applied and nothing is substituted;
* a sibling plasma family with no manifest is unaffected;
* generation, loading and the rate law itself are untouched.

**One measured refinement to the criterion argument, stronger than the version above.** The root
rule is written as an `Arrhenius` in `rules.py` and is an **`ArrheniusEP` once loaded**. So an
`appliesToKineticsClass = "Arrhenius"` manifest would not merely be direction-dependent — its
`affected_entries` reports **0 of 1 rules**. It would read correctly in the file and gate nothing.
That is pinned as a test by constructing the hypothetical `Arrhenius` quarantine in memory and
asserting it covers nothing.

**Two things the quarantine does *not* buy.** It is not a repair: the channel remains
unrepresented, which is the honest outcome but still a hole in the chemistry. And it is only as
real as the runtime — where `rmgpy/data/kinetics/quarantine.py` is absent the manifest is an inert
data file. Unlike `Cation_R_Recombination`, this family has **no declared-configuration fallback**:
it belongs to no set in `input/kinetics/families/recommended.py`, so it is reached only by being
named, and once named the gate is the whole of the protection. `test_eii_quarantine.py` therefore
*asserts* the loader is present rather than skipping without it, and asserts the family is in no
set — if it is ever added to one, the manifest matters more, not less.

**Merge position.** Unchanged in substance, and one of its two conditions is now met: the family is
refused admission. The engine hole is still open and still not this branch's to close. The
thermochemistry is sound and was never what was blocking.

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

**What the switch moved, recorded here and nowhere else (round 59).** §13.4 changed numbers in
other sections and, for one pair, the correction was written without removing what it superseded —
so §8's anchor disclosure and the entry's own longDesc carried *two* pairs with nothing to say
which was live. That is worse than the original error and is now fixed: the live pair appears once,
in §8 and in the entry, and the superseded pair appears once, here.

| quantity | `ThermoData` form (superseded) | `NASA` form (live) | exact |
|---|---|---|---|
| ΔH298(Ar → Ar(³P₂)) | 1114.2470 (+0.0002) | **1114.2439 (−0.0029)** | 1114.2468 kJ/mol |
| ΔS298(Ar → Ar(³P₂)) | 13.5027 (+0.1211) | **13.4922 (+0.1106)** | 13.3816 J/(mol·K) |

Both moved for one reason. The old form carried the same +0.0031 kJ/mol / +0.0105 J/(mol·K)
298-vs-298.15 K field offset as `BurkeH2O2`, the winner of the ground-state lookup, so in a
*difference* the two offsets cancelled and each residual was a file-value comparison. A `NASA` has
no such field, so neither cancels: the enthalpy residual became the winner's offset showing through
and the entropy residual *shrank* by that same offset. The asymmetry §8.3 warns about, visible in
this entry's own disclosure.

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
| `test/test_argon_metastable_thermo.py` | **44 passed** |
| `test/test_eii_quarantine.py` | **14 passed** (new) |
| `test/` (whole repository) | **273 passed, 3 failed** — the same 3 as before this work, a strict **subset** of the 4 failures carried by this branch's base `04846619b`; no new failure. All 4 are repaired at plasma head and green after §16's rebase |
| `test/database/databaseTest.py`, `database.directory` pinned at this worktree | **6 passed** in 490.9 s, *with the manifest in place* |
| `round58_probe.py` (re-run against the shipped `NASA`) | exit 0 |
| `quarantine_probe.py` | exit 0, every in-probe assertion passed |

Every run captured both streams into `docs/argon-metastable-thermo/logs/`.

Still in no deck. No rate, reaction, training entry or group was written or edited. One file was
added under `input/kinetics/` — the quarantine manifest, on the owner's explicit ruling, and it
refuses data rather than supplying any. Not pushed, not merged, no pull request.

*(§13.9's counts are round 58's and are superseded by §14.9. The sentence above about no group
being edited is superseded by §14.1: round 59 added one `forbidden` group to each of five
families, in a separable commit.)*

---

## 14. Round 59 — the reachability claim, and four smaller things

Five defects came back. One was the claim the library made about its own reachability; the review's
measurement of it was right in direction and wrong in size, in both directions, and the corrections
are recorded below with the numbers. Every new or repaired check in this round was shown **red**
against broken shipped data and then green, with both runs in
`logs/red_green.stdout.log` — 13 cases, 13 demonstrated, every restore verified by SHA rather than
by `git`.

### 14.1 HIGH — "exactly one family reaches it" was false, and the review's figure was also wrong

**The claim.** The entry said that of the six plasma families, one reaches this species, and the
library repeated that as "exactly one family reaches it". The six numbers behind it were correct.
The denominator was six, and this database ships **140** loadable families.

**Reproduced independently before touching anything**
(`all_family_reachability_probe.py`, then `silent_number_probe.py` with 50 partners):

| | |
|---|---|
| family directories on disk | 141 (140 + `__pycache__`) |
| families loaded by `load_families(families='all')` | **140** |
| ordinary gas-phase partners tried | **50** |
| families that generate from `Ar(3P2)` | **6** |
| reactions generated | **67** |
| reactions carrying a product whose thermo raises | **66** |
| reactions whose products all resolve | **1** — the intended ionisation, already quarantined |
| distinct first-generation products | 66, of which **57 raise** and 9 return a number |

**Two corrections to the review's own figures, both in its favour and against it.** The review named
five *partners* (H, OH, CH₃, O₂, N₂) and two families. Measured: **six families**, five of them
ordinary — `Birad_R_Recombination`, `R_Addition_MultipleBond`, `Disproportionation`,
`CO_Disproportionation` and `Cl_Abstraction`. The last three were not in the review's table at all,
and `Disproportionation` matters most of the three because it produces `[ArH]` directly. So the
problem is larger than reported, not smaller.

**Is it in a deck a real user gets?** Four of the five are in `recommended.py`'s `default` set — the
set a deck gets when it names no families. Only `Cl_Abstraction` is not. Ending 3 of the review
("show the reachability is not reachable in practice") is therefore dead, and it is dead on a
measurement rather than on a judgement.

**The "silent bad rate" case was searched for specifically, and it does not exist.** Answered
structurally rather than by trying partners until one stopped failing:

1. RMG refuses `1 Ar u0 p3 c0 {2,S}` outright — *"Invalid valency for atom Ar (Ar0s)"* — so a
   **neutral argon carrying a covalent bond is necessarily a radical**;
2. a radical's thermo is estimated by HBI, which saturates the radical site first;
3. saturating a one-bond argon gives a two-bond argon, and no atom type exists for that.

So it cannot be a number, by construction rather than by exhaustion. The 50-partner sweep agrees:
of 67 reactions, exactly one has all products resolvable and it is
`Plasma_Electron_Impact_Ionization`'s `Ar(3P2) => Ar+`, which the manifest already refuses. **The
failure mode is loud. Reported as asked, in both directions.**

**The ending chosen: close it at the family layer, and disclose it.** Round 59 proposed this as
"close it, disclose it, escalate the root cause to the engine"; the owner's ruling of 2026-09-21
struck the third clause, because there is no engine defect to escalate. See §14.2 — the closure is
the fix, not a holding action.

*Why a quarantine could not have been the answer, measured not argued* (`job_level_crash_probe.py`):
`CoreEdgeReactionModel.process_new_reactions` on `Ar(3P2) + H` with the `default` families loaded
raises `AtomTypeError`, unpatched; `CH3 + H` through the identical path completes. Instrumenting
both functions shows product thermo is generated inside `make_new_species` (`model.py:569` →
`:401`) **before** the first `apply_kinetics_to_reaction` (`:628`). A manifest would have refused a
rate the job never survives to ask for.

*What does work.* Each family's own `forbidden(...)` mechanism, which fires inside
`__generate_product_structures` — on reactants at `family.py:1669` and on products at `:1690` —
during generation. `Birad_R_Recombination` already uses it, and its existing entries say why in
their own words: **"This family is intended to handle [O] u2 p2, or [S] u2 p2, or [NH] u2 p1,
instances with a different number of lone pairs are forbidden."** `Ar u2 p3` is exactly such an
instance, so this writes down a rule the family already claims about itself.

*The label is load-bearing and silently so.* `ForbiddenStructures.is_molecule_forbidden` honours
atom labels, so an **unlabelled** `1 Ar u2 p3 c0` group matches nothing during generation — by then
the molecule's argon is tagged and cannot map to an unlabelled group atom. Measured both ways: the
unlabelled version left every reaction in place and looked like a working fix. The shipped entries
carry `*2`, `*3`, `*1`, `*1`, `*3` respectively.

*Measured with the containment in place* (`containment_probe.py`):

```
ordinary families still reaching Ar(3P2)     0   (was 5)
Plasma_Electron_Impact_Ionization survives   yes
control reactions that disappeared           0   of 22
```

The controls are what each family exists **for**; `Birad_R_Recombination`'s three are the ones its
own longDesc names — `[O] + [CH3]`, `[S] + [CH3]`, `[NH] + [CH3]`, all unmoved. One control,
`[H] + HCl` under `Cl_Abstraction`, reads zero with and without the containment: it is the
degenerate identity reaction. That was measured on the reverted file rather than assumed, and it is
recorded in the probe rather than dropped from the control list.

*The blast radius, stated because it is the reason for the commit structure.* Five ordinary families
that every RMG user loads, four in `default`. It lands as **its own commit**, five files and
nothing else, so the owner can drop it without touching the thermochemistry. If it is dropped, the
suite goes red at the tests that assert the containment — which is the intended behaviour, because
the entry's paragraph describing the containment would then be false and needs rewriting.

### 14.2 The `Ar0e` escalation, stood down — the atom types are correct

Round 59 ended by writing a hand-over paragraph asking the owner to commission a change to
`rmgpy/molecule/atomtype.py`. **The owner ruled on 2026-09-21 that there is nothing there to fix,
and the ruling is right.** This section replaces the escalation; the paragraph was never handed on.

**The ruling, in one line of arithmetic.** `u` is not a free parameter. Argon brings 8 valence
electrons, so for argon `8 − c = bonds + 2p + u` (the constant is argon's valence count, not a
universal one — oxygen's is 6). A bond-free neutral argon with three lone pairs therefore has
`8 − 0 = 0 + 6 + u`, so `u = 2`, and `Ar0e` at `p3 c0` **is** metastable argon — uniquely, not as
one reading among five. `atomtype.py`'s own comment that `Ar0e` "answers for five (u, p, c)
triples" is a statement about **group** patterns, where `ux` can be hand-written and nothing checks
valency. Families generate **molecules**. Round 59 read that comment at the wrong layer, and so did
the brief and the sparring round that raised the HIGH. The arithmetic was one line and nobody did
it, through three rounds of review.

**Measured, because a ruling is a premise like any other**
(`atomtype_u_determined_probe.py`, engine `RMG-Py-plasma@311818121`, exit 0):

```
u0  REFUSED   InvalidAdjacencyListError: Invalid valency for atom Ar (Ar0e) ...
u1  REFUSED   InvalidAdjacencyListError: ...
u2  ACCEPTED  atomtype=Ar0e  p=3  c=0  bonds=0
u3  REFUSED   u4  REFUSED
sweep over u 0–4 × p 0–4 × c −1/0/+1: total distinct triples perceiving as Ar0e = 1  (u2 p3 c0)
positive control — argon molecules built anywhere in the sweep = 3
8 − c = bonds + 2p + u:  Ar(3P2) 8 = 8 HOLDS   ·   Ar ground state 8 = 8 HOLDS
```

The uniqueness sweep is the block that could have refuted the ruling: any second triple would have
kept part of round 59's framing alive. There is none.

**What this changes, and it is the substance of round 60.** Every measurement from round 59 stands
— five ordinary families really do reach `Ar(3P2)`, the crash is real, the containment really does
close it with 0 of 22 controls moved. What changes is the **verdict** on them:

* The five `forbidden(...)` blocks are **the fix**, at the layer the error is on. Not a workaround
  held open pending an engine change. A family whose reacting site is a generic `R!H` at `u2`,
  which intends `[O] u2 p2`, `[S] u2 p2` or `[NH] u2 p1` and *says so in its own forbidden-group
  longDesc*, never encoded that restriction anywhere a matcher could read. The blocks encode it.
  This is a stronger claim than round 59's and it is the true one.
* **The incompleteness caveat stays and changes meaning.** A sixth family reaching this species
  would still reopen the crash — but it would be a family declaring a `u2` site broader than the
  chemistry it intends and shipping without saying so: a **family-authoring defect**, in that
  family, fixed the same way. Not an engine defect returning. Nothing in `atomtype.py` could
  prevent it, and no change there should be proposed on that basis.
* **Round 59's escalation probe is not withdrawn — it is re-read.** Its measurement (drop `R!H` →
  3 families still reach it; drop `R` → 2, channel lost; drop both → 0, channel lost) was correct
  and is now *corroboration*: no narrowing separates the wanted channel from the unwanted ones
  because there is nothing to narrow. The generality is not the error.
* **One round-59 statement is inverted outright** (§8 item 4, and the entry's STRUCTURE section).
  Round 59 repeated `atomtype.py`'s warning that `1 Ar0e ux p3 c0` "matches u1 argon as readily as
  the u2 metastable" without its layer. True group-against-group; unreachable in generation,
  because no u1 bond-free argon **molecule** exists to be matched. Block 4 of the probe shows it:
  four of the five `u` values have no molecule at all.

**What is *not* proposed.** No `rmgpy/` change of any kind, including a comment edit. The comment
at `atomtype.py:466` is accurate about what it describes; that it was misread at the wrong layer
twice — by a manager brief and by an adversarial round, before this session inherited it — is worth
the owner knowing, and it is the owner's call whether anything is done about it. It is recorded
here rather than raised as a ticket.

**A note on how this measurement nearly went wrong.** The first run of the probe printed a
confident, complete, **empty** answer: every molecule refused, including `u2`, which block 2 had
just built successfully. The cause was the probe's own formatting — `'c%+d' % 0` spells `c+0`,
which the adjacency-list parser rejects — so block 3 measured nothing and reported it as a fact
about the database. It was caught by the disagreement between two blocks of the same run. The
probe now carries a positive control (*"argon molecules built anywhere in the sweep"*, which is 0
exactly when the probe is broken) and asserts on it, because next time the two blocks might agree.

### 14.3 MEDIUM — the `2.0583e10` comparator had no citation and is withdrawn

The quarantine's justification quoted "a published state-resolved argon model, 2.0583e+10
m³/(mol·s)" and a **23.7-order** shortfall. Searched: that constant has **no citation and no
derivation anywhere in this repository**; `git log -S` finds it entering with this ticket's own
round-58 commits and nowhere earlier. It is withdrawn from both the entry and the manifest.

It is **not** replaced with another external number, and the reason is worth recording. The
state-resolved 1s5 expression offered in review, `6.8e-15 · Te^0.67 · exp(−4.2/Te)`, gives
**2.108e9** m³/(mol·s) at 3 eV if the prefactor is read as m³/s and **2.108e3** if it is read as
cm³/s — the convention such expressions are normally written in. Six orders of magnitude turn on a
unit convention only the source can settle. An uncited comparator has no place in an argument about
orders of magnitude, whichever way it points.

What replaces it is what the review recommended and what was always the stronger claim:

* **The quarantine rests on Te-independence alone.** The delivered rate is *bit-identical* at
  Te = 1 eV and Te = 3 eV. An electron-impact ionisation rate that does not depend on the electron
  temperature is disqualified by inspection, and that statement needs no external number.
* **For scale, an internal comparison:** this family's own rule evaluated at Te = 3 eV gives
  3.109200e+07 m³/(mol·s) against the 3.664598e-14 delivered at 1000 K gas — **20.9 orders**,
  measured entirely within this repository.

### 14.4 MEDIUM — §9's load-order hazard now has a detector

Reproduced: `BurkeH2O2` first → ΔS = 13.4922, residual **+0.1106**; `primaryThermoLibrary` first →
−0.00053; `NOx2018` first → −0.00076. The two existing tests pin the *rule* (first Ar-carrying
library in `library_order` wins) and the *identity* (the residual is that winner's own departure
from JANAF), and both are satisfied by whichever library happens to win — so neither would notice
the anchor moving.

`test_the_anchor_error_the_engine_delivers_is_the_one_the_library_discloses` reads the ΔH/ΔS pair
out of the entry's own text and compares it with what the engine delivers with every library
loaded. It goes red when the file drifts from the measurement — which is exactly how §13.4's
superseded pair survived — and when the resolved ground state changes. Shown red two ways (a
disclosed number moved; the superseded pair put back) and green.

**It does not close the hazard**, and the entry says so. Closing it means re-anchoring `BurkeH2O2`
or giving RMG a way to require a ground-state anchor; both are other tickets. It makes it loud.

### 14.5 MEDIUM — §13's correction left its old numbers shipped

Confirmed. The entry carried `dS = 13.5027 / +0.1211` — the `ThermoData`-form values — next to the
new ones, and the report described the emitted form as `ThermoData`. Both fixed: the live pair
(ΔH = 1114.2439, ΔS = 13.4922, residual +0.1106) appears once, in §8 and in the entry; the
superseded pair appears once, in §13.4, as history with the reason it moved. §5's "Form emitted"
paragraph and §10's `ThermoData` sentence now say what is true today and point at §13.4.

### 14.6 LOW — five tests that could not detect wrong shipped data

All five confirmed. Four recomputed module constants and never read the entry; the fifth declared
an `entry` argument and never touched it. Repointed, and each shown red against broken shipped data:

| test | now reads | shown red by |
|---|---|---|
| `..._level_energy_in_ev_matches...` | the entry's H298, back through `H = E·h·c·N_A` | moving `a6` |
| `..._two_metastable_levels_are_separated...` | the entry's own alternatives table | moving the 1s3 row |
| `..._r_ln_q_alone_understates...` | the table, plus the three magnitudes in the entry's prose | moving `R*ln term` |
| `..._where_the_lumping_difference_crosses...` | the table, the entry's four crossing temperatures, and the precision its S298 is written to | moving a crossing |
| `..._thermodata_freezes_entropy...` | the shipped Cp/H298/S298, and asserts the NASA *raises* out of range where a ThermoData freezes | moving `a1` |

### 14.7 The correction to my own §5 — accepted in full

"Three numbers, one identity each" was presented as though three independent things had been
checked. They are not independent: `H` is the ASD level energy times `h·c·N_A`, the eV cross-check
divides the *same* energy by a unit conversion, and `S` combines the *same* level's `J` with JANAF's
ground entropy. They validate the arithmetic, not the physics, and none of them would notice the
wrong ASD level having been transcribed. §5 and the entry now say so. Same shape as the
`1213 × 0.0085` withdrawal three days ago on I-235.

### 14.8 One thing the review got wrong, reported as asked

The review's Defect 1 header says "Five more do". Measured: **two** more families in its own partner
set, and **five** more across 50 partners — the count of *families* is 6 of 140, not 6 of 6 and not
2. The review's table lists 2 families over 5 partners; the extra three (`Disproportionation`,
`CO_Disproportionation`, `Cl_Abstraction`) it did not have. The direction of the finding stands and
the defect is worse than reported.

### 14.9 Checks run

| check | result |
|---|---|
| `test/test_argon_metastable_thermo.py` | **53 passed** (was 44) |
| `test/test_eii_quarantine.py` | **14 passed**, unchanged |
| `test/` (whole repository) | **281 passed, 4 failed** against the **272 passed, 4 failed** baseline *of this branch's base `04846619b`* — the same four failures, no new failure. That baseline is the BASE, not the project's head; all four are repaired at head and green after §16's rebase |
| `red_green.py` | **13 cases, 13 shown red then green**, every restore SHA-verified, exit 0 |
| `containment_probe.py` | 0 ordinary families reach `Ar(3P2)`, 0 of 22 controls moved |
| `atomtype_escalation_probe.py` | 4 candidates measured, no narrowing separates the wanted channel from the unwanted ones — re-read in §15 as corroboration that there is nothing to narrow |
| `test/database/databaseTest.py` (engine) | **6 passed**, 482.8 s — see §14.11 |

Round 60's own checks are in §15.3.

Both streams of every run are in `docs/argon-metastable-thermo/logs/`. Not pushed, not merged, no
pull request.

### 14.10 The red/green driver failed once, and what it cost

Recorded because it is the same class of defect this round was sent to fix, committed by the person
fixing it.

The driver was launched in the background, appeared to have died — its log was zero bytes and no
process matched — and was relaunched. **It had not died**; the log was empty because Python buffers
stdout when piped. Two instances then perturbed and restored the same four files concurrently. Each
verified its own restore by SHA against a baseline the other had already moved, so every case
reported red-then-green correctly *and* an `ArH` entry — a deliberately wrong covalent-argon thermo
entry, written to make one check fail — was left in `PlasmaExcitedNeutralThermo.py`. I committed it.

It was caught by re-running the full suite after the commit: 8 failed instead of 4, and the extra
four were the tests that the `ArH` entry exists to break, plus
`test_the_library_loads_alongside_every_other_thermo_library`, which asserts the library carries
exactly one entry. That last one is the reason it could not have shipped quietly, and it is a test
from an earlier round.

**The lesson is not "check the restores".** Every restore *was* checked. Per-case SHA verification
compares a file against a baseline, and a baseline is not a fixed point when something else can
write the file. Two guards were added:

* a **lock file**, so a second instance refuses to start; and
* a **contamination sweep** over every file the script can touch, for every marker it writes, run
  at the end regardless of how the cases went — plus positive checks for the two cases that
  *replace* rather than add, where there is nothing to grep for afterwards.

The sweep immediately paid for itself in a way worth recording: its first marker list included
`1 Ar u2 p3 c0` and `1 *2 R!H u2`, which are the entry's own molecule and
`Birad_R_Recombination`'s own `Birad` group. It refused to start, correctly, and the markers were
what was wrong. A guard that refuses on its first run is doing its job; the response is to check
whether it caught a real defect or exposed a false positive in itself, not to loosen it until it
passes.

Re-run clean, single instance, foreground: **13 cases, 13 red-then-green, 0 leftover
perturbations**, and the full suite back to 281 / 4.

### 14.11 The engine's own database suite, run against the containment

The unit suite shows the five contained families still generate the chemistry they exist for. It
says nothing about whether their *group trees* still satisfy the database's own structural
invariants, and a `forbidden(...)` block appended to a `groups.py` is exactly the kind of edit that
those invariants exist to catch. That suite is `test/database/databaseTest.py` in the engine, and it
is the one check round 59 had not re-run.

Run now, green:

```
6 passed in 482.81s (0:08:02)
```

— `test_kinetics`, `test_thermo`, `test_solvation`, `test_statmech`, `test_transport`,
`test_metal_libraries`, all PASSED, against round 58's baseline of the same six in 521.1 s. `stderr`
carries two `coverage` warnings and nothing else. Logs:
`docs/argon-metastable-thermo/logs/round59-databaseTest-{stdout,stderr}.log`.

**The pin is the part worth writing down.** `databaseTest.py` lives in the engine tree, so
RMG-database's `test/conftest.py` is never collected for it, and `database.directory` resolves to
the **shared primary checkout** — a run that ignores this worktree entirely and reports on somebody
else's tree. It was pinned with a one-line pytest plugin, and the plugin prints what it pinned and
refuses to load unless the containment and the library are actually present in that tree:

```
PIN database.directory = .../RMG-database-i221-argon-metastable-thermo/input
PIN containment present in Birad_R_Recombination/groups.py = True
PIN PlasmaExcitedNeutralThermo.py present = True
```

Those three lines are the head of the stdout log. Without them a green result here would be
unfalsifiable — the check cannot fail in the direction the defect lies if it is reading the wrong
tree. The suite was run from a scratch directory so that its `htmlcov/` and `.coverage`, neither of
which this repository ignores, land outside the worktree.

---

## 15. Round 60 — the owner's ruling: the argon atom types are correct

Round 59 closed with one thing outstanding: a paragraph asking the owner to commission a change to
`rmgpy/molecule/atomtype.py`. **It was never handed on.** The owner ruled on 2026-09-21 that the
atom types are correct as they stand, and the ruling is right — verified before anything was
written on top of it, in §14.2.

Nothing measured in rounds 55–59 changes. What changes is the verdict on it, and the verdict is
stronger than the one round 59 proposed.

### 15.1 What was ruled

`u` is not a free parameter. Argon brings 8 valence electrons, so `8 − c = bonds + 2p + u`, and a
bond-free neutral argon at `p3 c0` has `u2` and no choice about it. `Ar0e` in a **molecule** is
metastable argon uniquely — measured over the whole (u, p, c) grid, exactly one triple constructs.
`atomtype.py`'s comment that the type "answers for five (u, p, c) triples" is about **group**
patterns, where `ux` can be hand-written and no valency check runs. Families generate molecules.

So `Ar0e` being generic under `R`/`R!H` is not a defect, a family site written `R!H` at `u2` is
right to match this species, and **the five `forbidden(...)` blocks are the fix, at the layer the
error is on** — a family that intends three named biradicals and never encoded that.

The measurement, the probe, the uniqueness sweep and the one round-59 statement this inverts are
all in **§14.2**, which replaced the escalation in place.

### 15.2 What that changed in the shipped files

| where | from | to |
|---|---|---|
| five families' `forbidden` longDesc | "NOT THE ROOT CAUSE, AND NOT A SUBSTITUTE FOR IT" | "THIS IS THE FIX, AT THE LAYER THE ERROR IS ON", plus the arithmetic that licenses it |
| the same, incompleteness caveat | a sixth family reopens it (engine still owes a fix) | a sixth family would be a **family-authoring defect**, fixed the same way; no engine change would prevent it |
| `PlasmaExcitedNeutralThermo.py`, WHY THEY MATCH | the generics are why it matches, "nothing here can undo it" | the perception is correct; what is missing is the families' own statement of scope |
| the same, containment paragraphs | "WHY THAT IS NOT THE ROOT FIX" / "TWO THINGS THIS CONTAINMENT IS NOT" | "WHY IT IS THE FIX, NOT A WORKAROUND" / "WHAT THIS CONTAINMENT IS NOT: COMPLETE" |
| the same, STRUCTURE section | `Ar0e ux p3 c0` "matches u1 argon as readily" | true group-against-group, **unreachable** in generation — no such molecule exists |
| report §8 item 4 | the same unqualified warning | corrected, with the layer named |
| commit `5b194149d`'s message | "NOT THE ROOT CAUSE" | the stronger claim, and the retraction of the old one |

Commit `5b194149d` was rewritten rather than followed by a correction commit, because its message
is what an owner deciding whether to drop it reads. The five-file diff is byte-identical to the
original apart from the reframed longDesc paragraphs; nothing was pushed, so nothing downstream
was based on the old SHA (checked with `git branch --contains` and `git worktree list` first).

### 15.3 Checks run

| check | result |
|---|---|
| `test/test_argon_metastable_thermo.py` + `test/test_eii_quarantine.py` | **69 passed** (was 67: one repaired, two added) |
| `atomtype_u_determined_probe.py` | exit 0 — one triple perceives as `Ar0e`; positive control built 3 argon molecules |
| `u_determined_red_green.py` | green → red → green, no file touched |
| `red_green.py` | **17 cases, 17 shown red then green**, 0 leftovers, exit 0 |
| `test/` (whole repository) | **283 passed, 4 failed** against round 59's **281 passed, 4 failed** — the same four failures by name (of the *base*, `04846619b`; already repaired at head), and the two new tests. Superseded by §16: **318 passed, 0 failed** after the rebase |
| `test/database/databaseTest.py` (engine) | **6 passed**, 481.3 s, pinned to this worktree (the three `PIN` lines head the log). Re-run because this round changed the containment commit's *content*, not only its message |

Both streams of every run are in `docs/argon-metastable-thermo/logs/`, prefixed `round60-`. Not
pushed, not merged, no pull request.

### 15.4 Four things worth keeping

**A comment read at the wrong layer survived a brief, a sparring round and a full round of work.**
The `atomtype.py` comment is accurate about what it describes. It was applied to molecules, where
it does not hold, and the error was inherited rather than invented — the manager's brief carried
it, the adversarial round that raised the HIGH carried it, and round 59 acted on it. **The
arithmetic that settles it is one line and nobody did it.** *Probe the premise* is usually read as
"go measure the code"; this is the case where the premise was a sentence, and re-deriving its
claim from scratch would have cost less than the escalation it produced.

**A probe reported a confident, complete, empty answer.** The first uniqueness sweep refused every
molecule — including the one block 2 of the same run had just built — because `'c%+d' % 0` spells
`c+0`, which the adjacency-list parser rejects. It was caught only by the disagreement between two
blocks. The probe now carries a positive control (*argon molecules built anywhere in the sweep*,
which reads 0 exactly when the probe is broken) and asserts on it. **A sweep that finds nothing and
a sweep that cannot run look identical in a log.**

**The contamination sweep reported "clean" while blind.** `red_green.py`'s marker list was a flat
hand-maintained constant beside the case list; round 60 added four cases and the sweep — the guard
written *because* a perturbation once reached a commit — had never been told what to look for. It
is now keyed by case name, with an explicit `None` for the three cases that replace rather than add
text, and a startup assertion that refuses to run if the two lists drift. **A guard whose
configuration is maintained separately from the thing it guards decays silently, and reports
success while decaying.**

**One check could not be shown red by perturbing a file**, because what it guards is engine
behaviour and breaking it would mean editing `rmgpy/`. `u_determined_red_green.py` disables
`ConsistencyChecker.check_partial_charge` **in memory, in one process**, which is exactly the
counterfactual the test claims to catch — a future engine admitting a second `(u, p, c)` — and the
test goes red (`built {0: 'Ar0', 1: 'Ar0e', 2: 'Ar0e'}`), then green on restore. No file is
touched, and the restore is verified by object identity rather than by hash.

---

## 16. The four failures were never the project's — they were this branch's base

Raised by the manager on 2026-09-21, reproduced exactly, and correct in substance. This section
is the correction; every "pre-existing" in §7, §13 and §14 now points here.

### 16.1 What was wrong with the characterisation

Rounds 55–60 all reported the repository suite as *"N passed, 4 failed — the same four pre-existing
failures"*. Measured, that is true **against `04846619b`, the commit this branch was cut from**, and
false about the project. At plasma head `96f2afa4a` those four tests pass. The branch was carrying
the absence of a repair that had already landed, and the suite was faithfully reporting it.

**"Pre-existing" is a claim about a base, not about a project.** A reader who does not know which
base was meant will read it as the project's, which is the strongest available reading and the
wrong one. The phrase is removed in favour of naming the base every time.

### 16.2 One correction to the mechanism, in the manager's own spirit

The brief attributes the change to the I-223 merge. Measured, it is **I-234**:

```
git log --oneline 04846619b..96f2afa4a -- input/kinetics/libraries/PlasmaRadiativeRecombination/
    de27dd5c7  Make the uniqueness guarantee true, and correct four claims (I-234)
    9eeebedfa  Label the effect by observable, and refresh what the change made stale (I-234)
    2212f68ef  Withdraw the claims round 59 showed the evidence does not support (I-234)
    850c81cf0  Enter argon radiative recombination, and measure that it is not negligible (I-234)

git show --name-only 96f2afa4a -- input/kinetics/libraries/PlasmaRadiativeRecombination/   ->  empty
```

The I-223 merge (`96f2afa4a`) touches held-back `Plasma_Charge_Transfer` groups, training reactions
and test fixtures, and nothing under `input/kinetics/libraries/`. Everything else in the brief
holds: merge-base `04846619b`, head not an ancestor, and the net `input/` delta between the two is
exactly those two `PlasmaRadiativeRecombination` files, which are what the four failures exercise.

### 16.3 The rebase, and the prediction it was asked to refute

Rebased onto `96f2afa4a`; 15 commits replayed, no conflicts. The prediction held:

| | before | after |
|---|---|---|
| `test/` (whole repository) | 283 passed, **4 failed** | **318 passed, 0 failed** |
| `test/database/databaseTest.py` (engine, pinned) | 6 passed, 481.3 s | **6 passed**, 589.0 s |

`databaseTest.py` was re-run rather than assumed: the rebase brings I-223's held-back
`Plasma_Charge_Transfer` groups and I-234's library entries into the tree the containment is
loaded with, which is exactly the kind of change that suite exists to catch.

Nothing of this ticket's went red. The four named failures
(`test_the_dication_builds_and_raises_the_loud_databaseerror`,
`test_the_dimer_cation_builds_and_raises_the_loud_databaseerror`,
`test_argon_atom_type_now_declares_a_charge_envelope_but_still_parses_any_charge`,
`test_three_body_recombination_still_cannot_be_stored_at_all`) all pass. The count rises by 35
rather than 4 because I-223 and I-234 bring their own tests with them.

This ticket's files survived the rebase byte-identical — verified, not assumed:
`git diff <pre-rebase tip> HEAD` over the library, the five `groups.py`, the EII quarantine and the
test file is empty.

### 16.4 The collision the manager asked to have named rather than fixed

There is one, and it is **not** a code collision — the containment and the I-234 repair never touch
the same file. It is a **claims** collision, and I-234's text is the false side of it.
`input/kinetics/libraries/PlasmaRadiativeRecombination/reactions.py:347` ships:

> Argon's 4s `3P2`/`3P0` levels are metastable and make the point concrete: population reaching
> them is held, not delivered. **This database carries `Ar(3P2)` (`PlasmaExcitedNeutralThermo`,
> I-221) but no reaction reaches or leaves it**, so the branching cannot be represented here
> whatever its value.

Both halves are false, in opposite directions, and which half fails depends on where you stand:

* **At plasma head, where that sentence shipped:** `input/thermo/libraries/PlasmaExcitedNeutralThermo.py`
  **does not exist** (`git cat-file -e 96f2afa4a:...` fails). The database does not carry `Ar(3P2)`.
  The sentence forward-references an unmerged branch as though it were already in.
* **On this branch, where the library does exist:** *"no reaction reaches or leaves it"* is the
  exact claim I-221 round 59 retracted after measuring it. `Plasma_Electron_Impact_Ionization`
  generates the stepwise ionisation channel **out of** this species, and before the containment
  five ordinary families reached **into** it. `test_exactly_one_PLASMA_family_reaches_it_which_is_not_the_same_as_one_family`
  pins it and passes on the rebased tree.

**Not fixed here.** It is I-234's file, its claim, and its ticket; editing it would be exactly the
quiet fix the manager asked not to receive. Named for the owner. Note also the shape: I-234 states
something about a library that only exists on another branch, so it is *unfalsifiable in its own
repository* — the same absence-justification class as §11, arriving from the other side.

### 16.5 What this is an instance of

A merge in one place silently changed what a suite measures in another. Yesterday it was a merge in
the engine repository changing a database suite's result; here it is a merge in this repository
changing what this branch's own baseline means. **A baseline is a claim with an expiry date, and
the expiry is somebody else's merge.** The durable form: never report a failure count without
naming the commit it is relative to, and re-derive the baseline against *head* rather than against
the branch point before calling anything pre-existing.

### 16.6 One thing left uncorrected, deliberately

Four commit messages already on this branch — `b66346d3a`, `25bdb96e8`, `3ae1ade8a`, `5e905e506`
(post-rebase SHAs) — carry the superseded phrasing. Nothing is pushed, so they could be rewritten;
that is a second history rewrite across the branch for a phrase this section now corrects
authoritatively, so it is left as the owner's call rather than taken unilaterally. The tip's
message carries the correction.

---

## 17. Round 77 — the containment was sample-complete, and is now derived

Round 77's HIGH, reproduced and upheld. The verdict of round 60 stands untouched — the atom types
are correct, the family layer is where the fix belongs — but the *set of families* that fix was
applied to was found by sampling, and sampling missed six.

### 17.1 What was wrong with how the set was found

`all_family_reachability_probe.py` iterates all 140 families against a **hardcoded partner list**:
H, OH, CH₃, O₂, N₂ and the like. It is **exhaustive in families and a curated sample in partners**,
and it reported the sample's properties in the exhaustive axis's voice — "families matching
Ar(3P₂): 1". It could not have found `Br_Abstraction` (needs HBr), `F_Abstraction` (needs HF),
`Disproportionation-Y` (needs a fluorinated radical) or `Surface_Adsorption_Double` (needs a vacant
site), because no such partner was in the list. The all-families test had the same shape, hardcoding
the five already-known witnesses: a check that could not fail when a sixth family matched, and six
did. **The eleventh unfailable check this campaign has filed.**

**The tell was free and went untaken for two rounds:** `Cl_Abstraction` was forbidden while its
structurally symmetric siblings `Br_Abstraction` and `F_Abstraction` were not. A set that covers one
sibling and not the other two was sampled, not derived, and noticing that costs one `ls` of the
families changed.

### 17.2 The derived set is eleven, not nine

`template_space_derivation.py` asks the **shipped matcher** — `_match_reactant_to_template`, the
same call `__generate_reactions` makes — whether each per-reactant template site admits
`Ar u2 p3 c0`. No partner, no product, no imagination.

| family | direction | slot | before round 77 |
|---|---|---|---|
| Birad_R_Recombination | forward | 1 | forbidden |
| R_Addition_MultipleBond | forward | 1 | forbidden |
| Disproportionation | forward | 0 | forbidden |
| CO_Disproportionation | forward | 0 | forbidden |
| Cl_Abstraction | forward | 0 | forbidden |
| Br_Abstraction | forward | 0 | **open** |
| F_Abstraction | forward | 0 | **open** |
| Disproportionation-Y | forward | 0 | **open** |
| Surface_Adsorption_Double | forward | 0 | **open** |
| Cation_NO_Substitution | **reverse** | 1 | **open** |
| Li_NO_Substitution | **reverse** | 1 | **open** |
| Plasma_Electron_Impact_Ionization | forward | 0 | intended channel |

**Eleven non-EII, against the brief's nine, and the delta is explainable rather than a
disagreement.** The brief decomposed *forward* templates. `generate_reactions` also enumerates the
**reverse** template for any family that is `reversible` and not `own_reverse` (`family.py:1882`),
and both extra families are. The number was an output, it came out larger, and this says so.

All six are now forbidden, each with the atom label **read out of the matcher's own mapping**
rather than chosen — `*3`, `*3`, `*1`, `*1`, `*2`, `*2`. An unlabelled or wrongly-labelled group
matches nothing during generation, so that field is load-bearing and is no longer a judgement.

### 17.3 Reachability before, refusal after — with the partner derived too

The bar was: every family added needs reachability shown BEFORE and refusal AFTER. Showing it with
hand-picked partners would repeat the defect, so `template_witness_probe.py` derives the partner
from the *other* slot of the same template via `make_sample_molecule()`.

| family | derived partner | before | after |
|---|---|---|---|
| Br_Abstraction | `Br` (HBr) | 1 reaction, product `Br[Ar]` raises | 0 |
| F_Abstraction | `F` (HF) | 1 reaction, product `F[Ar]` raises | 0 |
| Disproportionation-Y | `[CH2]CF` | 1 reaction, product raises | 0 |
| Surface_Adsorption_Double | `[Pt]` | **generation itself raises** building `Ar=X` | 0 |
| Cation_NO_Substitution | `[Li]N` | 2 reactions, reactant `[Ar]NH2+` has no thermo | 0 |
| Li_NO_Substitution | `[Li]N` | 2 reactions, same | 0 |

`Surface_Adsorption_Double` is the worst of the six: it does not produce a bad product, it raises
`AtomTypeError` *while constructing* `Ar=X`, before any product exists.

**Controls: 0 regressions across all eleven.** Three of the template-derived controls read 0
reactions with the block and 0 without — `make_sample_molecule()` hands back `[H] + HX`, and
`H· + HX → HX + H·` is the degenerate identity RMG never generates. **A control that reads 0 = 0
carries no information**, and counting it as passing is the very pattern this round was sent to fix,
so the probe now labels those VACUOUS by name and each of the three families gets a hand-written
control with a real partner in `CONTAINMENT_CONTROLS` instead.

### 17.4 A second failure mode, found by the two reverse-matching families — WITHDRAWN in round 80

The entry has argued since round 58 that this can never be a silent wrong number, structurally:
RMG refuses a neutral bonded argon at u0, so every covalent neutral argon is a radical, so its
thermo routes through HBI, which saturates it to a two-bond argon with no atom type.

Round 77 claimed the reverse-matching families escape that argument by building a bonded argon
**cation**, `[Ar]NH2+`, failing in the group-additivity lookup with `DatabaseError: no data for
node R or any of its ancestors` instead. **That claim is withdrawn: neither half of it matches
the executed path.** The cation was hand-built, not generated. What `Cation_NO_Substitution` and
`Li_NO_Substitution` actually generate is `N[Ar]` — a **neutral** bonded argon radical,
`Ar u1 p3 c0` bonded to N, net charge 0 — and it raises `AtomTypeError` from HBI saturation like
the other nine (`AtomTypeError` on a stock engine; `SaturatedStructureError`, the same failure
named, on the round-80 engine). See §18.3.

Why the wrong answer stood for a round: the witness probe's `thermo_verdict()` inspected
`reaction.products` only, and in a reverse match the bonded argon is a **reactant**. The probe
printed zero failures for both families while direct checking reproduced the raise, so the
mechanism was reconstructed by hand instead of read off the measurement. Fixed in round 80 —
`thermo_verdict()` now walks both sides and reports which side each failure sat on.

**The conclusion is unchanged and the argument is wider than it looked:** the three structural
steps cover all eleven families, and there is one loud failure route, not two.

### 17.5 The four standing items

| item | what was done |
|---|---|
| **Load-order anchor** — tests pinned whichever first-match anchor wins | `test_which_ground_state_argon_anchor_is_correct_and_which_one_wins` now decides. Ground-state argon is a monatomic ideal gas whose S298 is a Sackur–Tetrode number; JANAF Ar-001 gives 154.845. The carriers split into a correct camp (154.8459 — `primaryThermoLibrary`, `NOx2018`, …) and a wrong one (154.7323/154.7348 — `BurkeH2O2`, `JetSurF`, `GRI-Mech3.0`, …). The test asserts the correct camp is non-empty, that RMG's own default library is in it, and that **the runtime resolves into the wrong camp** — the defect pinned *as* a defect, red the day it is fixed upstream. It still does not close the hazard; it stops the suite being neutral about a question with a right answer. |
| **EII quarantine is runtime-dependent, no compatibility pin** | The manifest now carries a machine-readable pin — `requiresEngineModule`, `requiresEngineSymbol`, `requiresEngineCommit = 541e6498f` (RMG-Py, 2026-08-25, "hard-fail when quarantined database data reaches a reaction model") — and a `bypassRoutes` tuple enumerating the four routes that go around it: an engine without the module, a direct database consumer reading `.kinetics`, an equivalent rate via reaction library or seed mechanism, and anything reading `rules.py` as a file. Two tests assert the pin is complete, that **this** runtime satisfies it (an assertion, not a skip — a run on an unguarded engine must fail loudly), and that the bypass list stays enumerated. |
| **`2.0583e10` withdrawn in the report, still driving assertions** | Withdrawn for real. The constant is deleted; the comparator is now this family's **own rule evaluated at Te = 3 eV against what it delivers at Tgas = 1000 K**, > 20 orders, measured entirely inside this repository — which is what the report already said replaced it. It survives only in a comment explaining its withdrawal. |
| **Header still warned "until the engine atom-type gap is fixed"** | Withdrawn, twice over: there is no engine-side gap (round 60), and the database-side fix is now complete against the shipped template space. The header now says loading this library beside ordinary combustion families is what the containment is *for*. |

### 17.6 Checks run

| check | result |
|---|---|
| `test/test_argon_metastable_thermo.py` + `test/test_eii_quarantine.py` | **73 passed** (was 69; four added) |
| `template_space_derivation.py` | **exit 0** — 12 families admit, 11 forbidden, 1 intended; controls pass |
| `template_witness_probe.py` | 11 witnesses, 11 refused after, **0 control regressions**, 3 vacuous controls named |
| `red_green.py` | **22 cases, 22 shown red then green**, 0 leftovers, exit 0, stderr empty (five cases are new) |
| `test/` (whole repository) | **322 passed, 0 failed** against round 61's 318 — the four added here, no regression |
| `test/database/databaseTest.py` (engine, pinned) | **6 passed**, 466.1 s. Re-run because this round edits a SURFACE family (`Surface_Adsorption_Double`) for the first time |

### 17.7 What this round got wrong first, twice

**The first derivation returned six families and was confidently wrong.** It treated each template
*entry* as one reactant's site. Every modern abstraction family — `Cl_Abstraction`,
`Br_Abstraction`, `F_Abstraction`, `Disproportionation`, `CO_Disproportionation` — ships **one**
entry called `Root` spanning the whole bimolecular complex (`reactantNum = 2`, 3–4 atoms), so
matching a single molecule against it can never succeed. The probe reported "no match" for exactly
the families that do match, and would have *removed* three containments that were already right.

What caught it was **disagreement with an older measurement**: the six-family answer excluded three
families this ticket had already forbidden on measured evidence. RMG splits the Root at
`family.py:2085`; the probe now mirrors that rather than assuming a shape.

**The second was the vacuous control**, above. Both have the same shape as the defect the round was
sent to fix: *a procedure that cannot see the thing it is looking for, reporting that the thing is
not there.* Three instances in one campaign — a partner list that could not reach four families, a
template decomposition that could not see Root families, a control that could not distinguish
"unchanged" from "never happened". The lesson is not "be careful"; it is that **every enumeration
needs a stated axis and a control that fails when the axis is wrong**.

### 17.8 An operational note on the red/green driver's own guards, both of which fired

The driver refused the round-77 case *"the entry stops naming the anchor that is CORRECT"*,
because its anchor string `primaryThermoLibrary` occurs four times in the entry and the driver
requires exactly one. That refusal was correct and it exposed a weaker test: the assertion it was
meant to break keyed on the bare library name, which appears four times for four different reasons,
so the claim could have been deleted with the test staying green. The assertion now keys on the
sentence that makes the claim. **The guard did not merely block a bad perturbation; it found a bad
assertion.**

**A third guard failure, found by the second guard.** Two round-77 cases named tests that live in
`test_eii_quarantine.py`, while the driver hardcoded one suite. pytest was handed
`test_argon_metastable_thermo.py::test_the_manifest_declares...`, could not collect it, and exited
non-zero — which the driver read as RED. The perturbation was never the reason. It surfaced only
because the restored GREEN run failed identically; **had the restored run passed for any reason at
all, the case would have reported a clean red-then-green for a test that never executed.** A driver
whose whole job is to prove that tests can fail must not be able to fake a failure. It now resolves
each test name to the file that defines it by scanning what is on disk, and asserts the name exists.

The crash then left the lock file behind, and the next run refused to start — also correct, and the
reason the lock exists. Worth writing down because the recovery is not obvious: a driver that dies
inside a case leaves a lock naming a PID that no longer exists, and the only safe clearance is to
confirm the PID is dead before removing it. This is the
second time this campaign's own tooling has caught this campaign's own mistake.

---

## 18. Round 80 — the HIGH was an engine defect, and four standing items

Round 80's finding is not in the database. Transport estimation and solute-data estimation both
die on metastable argon, at a layer a kinetics family cannot reach: they fire **after** the
species is admitted, and neither transport nor solvation is a family. Both were fixed in RMG-Py,
on a dedicated worktree and branch.

### 18.1 The premise, reproduced before anything was built on it

The brief's claim was reproduced first, with the controls that make it falsifiable — `scratchpad/
saturation_probe.py`, run in both directions:

| species | transport | solute data |
|---|---|---|
| `Ar u2 p3 c0` | `AtomTypeError` | `AtomTypeError` |
| `Ar u0 p4 c0` (control) | survives, library `NIST_Fluorine` | survives, solute library `Ar` |
| `[CH3]` (control) | survives | survives |

**Two line numbers in the brief are one hop off, and the defect is the brief's.** The raising
lines at engine `273f38bfa` are `transport.py:465` and `solvation.py:1566`, not `:459` and
`:1424`; those are in the enclosing functions. Recorded because round 77's lesson was to
reproduce a brief's numbers and say the delta out loud.

### 18.2 The cause, and why it is fixed as a cause

**Radical saturation of a species whose saturated form no atom type owns.** Every
hydrogen-bond-increment estimator — thermo, transport, solute data — builds a saturated copy as an
intermediate, which assumes each radical electron is an unfilled chemical valence. For an
electronically excited atom it is not. `Ar u2 p3 c0` saturates to ArH2: electron-count-consistent
and owned by nothing. Ground-state argon survives because `u0` saturates to itself.

`rmgpy/data/base.py` gains `saturate_for_estimation`, which does what all five call sites did
inline and raises `SaturatedStructureError` — naming the species, its saturated form, the estimate
that could not be made, and what to supply instead — when the saturated form has no atom type.
Four call sites adopt it (transport, solvation, thermo, uncertainty); `rmgpy/qm/main.py` is the
fifth and is left alone, guarded by `onlyCyclics` and unreachable for a monatomic. **Round 87
reversed that last decision** — it is now routed through the helper too, so all five adopt it.
See §20.5.

**The two candidate approaches, and the judgement.** Shipping transport and solute data for this
species is smaller and was proved to work. It was **not** taken as the fix, for two reasons. It
covers only species somebody anticipated, while the defect is in the estimator and reachable by
any future species of this shape. And there are no sourced Lennard-Jones or Abraham parameters
for Ar(4s ³P₂) in hand — copying ground-state argon's would put an unsourced number into a
campaign that has refused exactly that repeatedly. What the estimators do instead:

- **transport falls back**, to the Lennard-Jones estimate the group estimator already falls back
  on for every other failure — and says so, in a warning and in a comment that reaches `tran.dat`:
  *"these parameters are a heavy-atom-count guess and nothing more."* The deck completes.
- **solute data reports rather than invents.** There is no defensible Abraham estimate for a
  metastable noble gas, so it raises — but with the species and the remedy named, instead of an
  `AtomTypeError` from many frames below the call the modeller made.

### 18.3 What the consumers do, measured end to end

`scratchpad/consumer_endtoend.py` drives the three consumers the brief names, on both engines.
Before: the first one crashes. After, all three complete and the reason survives into the output.

| consumer | before (`273f38bfa`) | after |
|---|---|---|
| `Species.get_transport_data()` | `AtomTypeError` | σ = 3.758 Å, ε/k = 148.6 K, comment carries the reason |
| `save_transport_file` (tran.dat) | never reached | renders, with the reason as the entry's comment |
| `Configuration.calculate_collision_frequency` (pdep) | never reached | 2.601e9 Hz at 1000 K, 1 atm |

Ground-state argon is the control throughout and keeps its library values (σ = 3.33 Å,
`NIST_Fluorine`).

### 18.4 Which other shipped species have this shape: **one, and it is ours**

`scratchpad/unsaturable_species_survey.py` enumerates every species the shipped databases name —
79 thermo libraries, 5 transport, 2 solute, 188 kinetics libraries — and tests each for the shape.

**26,210 distinct structures scanned; 1 hit: `Ar(3P2)`, in `PlasmaExcitedNeutralThermo`.** The
answer today is "none but the one this ticket adds", and that is worth stating because it tells
the next reader what changes the day a second one appears.

Two things bound it. The survey covers the species databases *name*, not species RMG can
*generate* — generated ones are the family-layer containment's job. And the shape is narrower
than "excited species": tested directly, **metastable neon `Ne u2 p3 c0` saturates cleanly**,
because RMG's `Ne` atom type carries no bond or lone-pair constraint, while argon's `Ar0e` does.
Ne\* would therefore reach the same Lennard-Jones fallback by the ordinary `KeyError` route and
get the same numbers **with nothing said about why** — quieter than argon's failure, not safer.
Named, not fixed: atom types are the owner's closed item (round 60).

### 18.5 The four standing items

| item | what was done |
|---|---|
| **MEDIUM — the EII pin is not enforced** | It is now. `load_family_quarantine` imports the declared `requiresEngineModule` and looks up `requiresEngineSymbol`, refusing the load with a `DatabaseError` naming the family if either is absent. `requiresEngineCommit` is **deliberately not checked** and is relabelled provenance: an installed engine has no reliable commit to compare against, so a commit check would pass on every checkout — a check that cannot fail. The declared symbol also changed, from the loader (`load_family_quarantine`) to the **gate** (`check_quarantine`): the loader reading a manifest was a tautology, while the gate is what makes the refusal real. The database-side test asserts the *enforcement*, not the declaration, and is red on an engine that only declares. |
| **MEDIUM — the anchor test pinned the defect** | Asserting "the runtime resolves the WRONG camp" makes a defect the expected state and turns the day somebody fixes it into a red suite. The decision is asserted instead: the entry must quote the **JANAF-anchored** excitation pair (1114.2468 kJ/mol, 13.3816 J/(mol·K)), and the load-order hazard is asserted as a disclosure that must be present while it is live and absent once it is not — correct under both states, satisfiable by silence under neither. On the resolution: `BurkeH2O2`'s 36.98 cal/(mol·K) is the published mechanism's own four-figure value, faithfully transcribed. A library that reproduces its source is doing its job; the gap belongs at the **selection** layer, and that is still upstream. |
| **LOW — `thermo_verdict()` inspected one side** | It walked `reaction.products` only, so for the two reverse-matching families — where the bonded argon is a generated **reactant** — it printed zero failures while direct checking reproduced the raise. It now walks both sides and labels which side each failure sat on. This is the same width failure as round 77's partner list: a procedure that cannot see the thing it is looking for, reporting that the thing is not there. |
| **LOW — the withdrawn `2.0583e10`** | Gone from `round58_probe.py`. The comparator is now this rule against itself — evaluated at Te = 3 eV versus delivered at Tgas — which is what the report already said replaced it. The constant survives only in a comment explaining the withdrawal. |
| **LOW — the header said five families** | Corrected to eleven (twelve admitting, one of them the intended EII channel), with the method named: derived from the template space, not counted over a partner sample. The test whose *name* said "five containments" is renamed and its docstring keyed to `CONTAINED_FAMILIES` rather than to a count. |
| **LOW — the derivation swallowed matcher exceptions** | A raising matcher meant "does not match", which quietly narrowed *every family whose template admits it is contained* to *every family whose template could be evaluated*. Raises are now collected in `MATCHER_ERRORS`, reported as UNDETERMINED, and fatal. Shown able to fail: with one family's matcher sabotaged, the derivation reports 8 unevaluable slots and exits 1. |

### 18.6 A withdrawal: the "second failure route" never existed

Round 77 wrote into the entry that the two reverse-matching families build a bonded argon
**cation**, `[Ar]NH2+`, failing with `DatabaseError: no data for node R or any of its ancestors`
rather than `AtomTypeError` — a second loud route the structural argument did not cover. **Both
halves are wrong.** Measured through the families' own generation, the species they build is
`N[Ar]`: a **neutral** bonded argon radical, `Ar u1 p3 c0` bonded to N, net charge 0, which raises
`AtomTypeError` from HBI saturation exactly like the other nine.

The cation was hand-built, not generated. It stood for a round because the probe that should have
caught it inspected products only (§18.5) — so the mechanism was reconstructed by hand instead of
read off the measurement. **The conclusion is unchanged and the argument is wider than it looked:**
three structural steps, eleven families, one loud failure route.

### 18.7 Checks run, and what each is relative to

The plasma engine moved twice during this round: `311818121` → `273f38bfa` (§5a of the round-77
handoff) → **`40e21b495`** (I-244, which changed `chemkin.pyx`, so the built extensions were
refreshed). The engine branch was rebased onto `40e21b495` and everything re-measured there.

| check | result | relative to |
|---|---|---|
| database `test/` | **323 passed** | database `0c75e1c79` + this round, engine branch `8ff42bd1a` |
| database `test/` on the **pristine** engine | 322 passed, **1 failed** — the pin-enforcement test, by design | engine `40e21b495` |
| `template_space_derivation.py` | **EXIT 0**, 12 admit / 11 forbidden / 1 intended, no unevaluable slot | as above |
| engine `saturatedStructureTest.py` (new) | **12 passed**; shown **4 failed** with the two call sites reverted | engine `8ff42bd1a` |
| engine `quarantineTest.py` | **33 passed, 7 skipped**, against 29/7 pristine — the 4 new ones | engine `40e21b495` → `8ff42bd1a` |
| engine transport/solvation/thermo/base/uncertainty | identical on both engines, including the **2 thermoTest failures that are the base's** | engine `40e21b495` |

**The database branch now requires the engine branch.** `test_this_runtime_ENFORCES_the_declared_
engine_requirement` fails on any engine that reads a manifest without honouring what it declares —
which is the point of it, and is the loud failure the manifest has always said it wants. §19 states
that requirement in full, for whoever merges.

---

## 19. MERGE REQUIREMENT — this branch does not stand alone

*Written for whoever performs the merge, and deliberately placed last so it is the final thing read.
Ruled on 2026-09-22; the alternatives were considered and are recorded in §19.3 so the decision is
not silently reversed by someone who did not see the history.*

### 19.1 The requirement, in three sentences

**(a) This branch requires the RMG-Py branch `i221-saturation-no-atomtype`** — two commits,
`e1b28b064` and `8ff42bd1a`, on plasma head `40e21b495`. Not "works better with": *requires*. On a
pristine engine this branch's own suite is **322 passed and 1 failed**.

*Amended by round 90 (§21): the branch is now **eight** commits on plasma head `98d465d3b`, tip
`e0f075780`; the SHAs quoted throughout §19 are the pre-rebase ones and survive only under the tag
`i221-pre-rebase-39336c8ab`. The pristine-engine figure is **322 passed and 2 failed** — both
failures are negative controls, measured on `98d465d3b`.*

*Amended by round 87: the pin this section describes was real but weaker than it claimed — a
manifest naming `math.pi` as its gate loaded clean. §20.4 records what was wrong and what the
enforcement checks now. The co-landing requirement below is unchanged and, if anything, firmer:
there are now four engine commits the database depends on, not two.*

**(b) The failing test is the negative control, and it is failing on purpose.**
`test_this_runtime_ENFORCES_the_declared_engine_requirement`, in `test/test_eii_quarantine.py`,
fails on exactly those engines that read `input/kinetics/families/Plasma_Electron_Impact_Ionization/
quarantine.py` and then ignore the `requiresEngineModule` / `requiresEngineSymbol` it declares. It
is the only thing in either repository that distinguishes a pin which is **enforced** from a pin
which is merely **declared**. A green suite here would mean the test cannot fail, which is the
defect this ticket's round-80 MEDIUM was filed to repair.

**(c) Landing the two separately, in either order, reopens the window.** Database first: the
manifest declares a requirement no engine honours, and it is a comment again until the engine lands
— with the one test that would say so failing, and therefore likely to be "fixed" by skipping it.
Engine first: the enforcement exists but nothing in the shipped database exercises it. **Co-land, or
the pin is decorative for the duration of the gap.**

### 19.2 What to do at merge time

Merge the branch, not a SHA list — the branch is the authority, and the list below is here only so
that a merge arriving short is visible. The database commits are `3ae1ade8a`, `833f6fe8a`,
`0c75e1c79`, `31a20f076`, `662cc393e`, `a2cf9cd84`, `5afb62d8b`, `9c88ea2b7`, and round 90's
`d51154ab1`, `1ac70d663`, `1c2d60dde`, `f5b0e83d4`. **The first of those was written here as
`17f3c4d57` until round 92 and that SHA is dead** — it is the pre-rebase twin of `3ae1ade8a`, same
message and same author date, and `git branch --contains` names nothing. A SHA list copied forward
across a rebase is exactly how a merge instruction rots; this one did.

They go together with the engine commits — **the post-rebase SHAs,
which are the only ones on the branch today**: `73c8214f7`, `4f5dff3db`, `88f080f80`, `d64029618`,
`2c445dfdd`, `2482ee8f0`, `25a8d9393`, `e0f075780`, plus round 90's logs-only `5d7d86738` and round
92's `14a4099bb` (probe) and `9b89a937c` (the repairs), sitting on plasma head `98d465d3b`. Re-run
the suite against the merged engine — the expected result is **324 passed**, measured at database
`f5b0e83d4` against engine `9b89a937c` (`logs/round92-db-suite.log`), not inherited from an earlier
pairing. A failure in
`test_this_runtime_ENFORCES_the_pin_as_more_than_an_attribute_lookup` or
`test_this_runtime_ENFORCES_the_declared_engine_requirement` says the engine half did not land, or
landed short. Nothing here has been pushed, and no merge on this campaign is the agent's act.

### 19.3 Why the two alternatives were refused

- **Skip the test on an unenforcing engine.** Refused. A `pytest.skip` that fires on precisely the
  engines where the pin matters *is* a check that cannot fail, and it is invisible in a pass count —
  the same defect class this campaign has now filed eleven separate times. It repairs round 80's
  MEDIUM by recreating it one layer down.
- **Move the enforcement test into the engine repository,** beside the code it guards. This one has
  real merit and was weighed seriously. It loses because the database would then declare a
  requirement with nothing in *its own* suite checking end to end, so the two can drift apart the
  moment the repositories move independently — which is the original disease, not a cure for it.

Option 1's cost is coordination, not correctness. The unpinned cross-repository pairing has been
raised as a MEDIUM on four adversarial rounds across two tickets, and every remedy proposed before
this one was a document or a proposal rather than a mechanism. A failing test is the first version
of it that cannot be ignored and cannot drift, stated in the only language CI reads.

### 19.4 The engine-side exception, since the report was asked for it by name

The engine transport work **was done**, on the branch above. It is not outstanding.

| | |
|---|---|
| **Class** | `SaturatedStructureError`, `rmgpy/exceptions.py:292` — a direct `Exception` subclass, deliberately **not** an `AtomTypeError` subclass, so no existing `except AtomTypeError` silently swallows it (asserted at `test/rmgpy/data/saturatedStructureTest.py:117`) |
| **Sole raise site** | `rmgpy/data/base.py:1348`, inside the new shared helper `saturate_for_estimation(molecule, data_type)` — the one place the saturation is performed, rather than five inline copies |
| **Adopted by** | all five saturation sites: `transport.py`, `solvation.py`, `thermo.py`, `tools/uncertainty.py` and — since round 87 — `qm/main.py`, which had been excused as unreachable for a monatomic and was still reachable for a cyclic non-valence radical (§20.5) |
| **Caught by** | `rmgpy/data/transport.py:352` and `:376`, which fall back to the shipped last-resort Lennard-Jones estimate and stamp the `tran.dat` comment with *"a heavy-atom-count guess and nothing more"*. Solvation deliberately does **not** catch — there is no defensible Abraham estimate for a metastable noble gas, so it reports instead of inventing |

**Does the message name the species and the call path?** Yes, both, and that was the point of the
change. The message interpolates: the species' **adjacency list** (not its SMILES — a `to_smiles()`
failure inside the handler would recreate the very undiagnosable crash being removed), its radical
count, the **saturated form's** adjacency list, the `data_type` the caller was actually estimating
(`'transport data'`, `'solute data'`, `'thermodynamic data'`, `'thermodynamic uncertainty'`), the
remedy — supply the data in a library entry or keep the species out of the model — and the
underlying `AtomTypeError` text, so nothing is hidden. It is raised at the saturation site, so the
traceback still carries the full call path; what changes is that the top frame now names the
species and the estimate instead of an anonymous atom and a bond count many frames below whatever
the modeller asked for.

Before this, a modeller whose deck contained `Ar(3P2)` got an `AtomTypeError` from inside transport
estimation naming neither the species nor the reason — the failure mode described in §18.1.

---

## 20. Round 87 — the gate was keyed on a slot a wrapper repurposes

Review of the engine branch at `8ff42bd1a`: no CRITICAL, one HIGH, two MEDIUMs, one LOW. What held
is not re-litigated here — the class hierarchy of `SaturatedStructureError`, transport's conversion
to the fallback, the caveat surviving into `tran.dat` at 3.758 Å / 148.6 K, and the reachability of
the solvation refusal. This section is the four that did not.

All eight findings below were reproduced before anything was built on them, by
`docs/i221-saturation/probes/round87_provenance_probe.py` in the engine repo: **8 of 8 reproduced,
4 of 4 controls holding** at `8ff42bd1a`, and **0 of 8, same controls** at the fix.

### 20.1 What a quarantine is actually about — asked before it was re-keyed

The review required this answered first, and it decides the shape of the fix.

**The quarantined thing is the RATE.** A `Marcus` rate with no electrochemical reference returns a
meaningless number wherever it is stored; an estimated EII rate is evaluated at `Tgas` wherever it
is stored. Copying either into a seed mechanism does not repair it. The family is in the key for
two reasons, and neither is that the family is what is wrong: it is **where the manifest lives**,
next to the data it describes, and it is **what scopes the criterion**, because
`appliesToKineticsClass = "Marcus"` on its own would ban a kinetics class across all of RMG,
including the legitimate electrochemistry the quarantine must not touch. The module's own design
already said this — `applies_to()` takes kinetics and nothing else, and `affected_entries()`
computes the set from the data — but the *gate* did not.

So the key is **(authoring family, kinetics criterion)**, and *authoring* is the load-bearing word:
it has to survive the rate being copied.

### 20.2 The HIGH, and the premise that inverted under it

`LibraryReaction.__init__` ends with `self.family = library` (`library.py:100`). One attribute,
two kinds of name: a family label on a `TemplateReaction`, a library label on a `LibraryReaction`.
The gate read it directly, so it failed in **both** directions — the review named the first, the
probe found the second:

| | before | after |
|---|---|---|
| quarantined `Marcus` rate copied into a seed (`library="copied_seed"`) | **admitted** | refused |
| innocent library that happens to share the family's name | **refused** | admitted |

The review anticipated that authorship might be unrecoverable once a rate is copied, and said that
if so the fix belongs where provenance is *lost*. **That premise was checked and it is false**,
which is what kept the fix at the read site. `KineticsLibrary.get_library_reactions`
(`library.py:355-372`) already parses a `family: <label>` line out of an entry's `longDesc` and
rebuilds the reaction as a `TemplateReaction` of that family — but only when the library is
`auto_generated`. Authorship is therefore usually **present and unread**, not absent: RMG writes it
into every estimated rate's comment, the library writer saves it, and `.family = library` then
overwrites the one slot a reader would consult.

`authoring_family(reaction)` now resolves it: `reaction.family` for a template reaction, and for a
library reaction the `family:` line from the kinetics comment or the entry's `long_desc`, never the
repurposed slot.

**What remains, named rather than papered over.** A hand-written library entry with no comment
carries no authorship at all, and nothing can recover it. There the gate cannot distinguish a
copied quarantined rate from an independent rate of the same class, and it **warns once per
(library, kinetics class) rather than refusing** — refusing on the criterion alone would ban
legitimate `Marcus` electrochemistry, trading a silent admission for a silent obstruction. The EII
manifest's `bypassRoutes` entry 3 is narrowed accordingly, from "an equivalent rate supplied
through a reaction library or a seed mechanism" to "hand-written library/seed entry with the
authoring-family comment stripped". That entry had written the hole off as a fact of life; it was
closable, and most of it is now closed.

### 20.3 Where this sits in a pattern the campaign keeps re-deriving

The review called it the seventh instance this week of keying on an attribute a wrapper repurposes,
and the first in a *gate* rather than a selector. The rule already on file is *key at the finest
identity the physics distinguishes*; the sibling it adds is **key on something a wrapper cannot
repurpose**. The tell here was available without running anything: `get_quarantine`'s own docstring
said a kinetics library "cannot carry a family manifest" and would "yield `None`" — which is the
bypass, written down as if it were a reassurance.

### 20.4 The pin was weaker than this report twice said it was

Round 80's enforcement was real; "the pin is now real" was an overstatement, and the manager has
recorded the same overstatement in the project record. Four holes, each reproduced:

| declared | before | now |
|---|---|---|
| `requiresEngineSymbol` with no `requiresEngineModule` | skipped in silence (`if not module_name: return`) | `DatabaseError` — a check that cannot be performed must not look like one that passed |
| a symbol that exists but is not callable | accepted; a manifest naming **`math.pi`** as its gate loaded clean | `DatabaseError` — a gate that cannot be called is not a gate |
| the symbol is reached from model admission | never checked; existence proves only that the capability was written | `requiresEngineCallSites` names modules that must bind **that exact object** |
| `requiresEngineCommit` | read and deliberately ignored | **not declarable** — `DatabaseError` naming the replacement |

The last one is the round-80 repair repeating one layer up, and worth stating plainly. Round 80
correctly concluded a commit check could never fail, and answered by documenting the field as
provenance in a comment while leaving it named `requiresEngineCommit`. **A reader greps the field
name, not the comment beside it.** The field is now refused outright; the commit moves to
`recordedEngineCommit`, which the loader reads and logs — because a field nothing consults is
exactly where this thread started.

### 20.5 The two smaller ones

**The message printed an adjacency list that could not be read back.** `saturate_radicals` assigns
`multiplicity` only *after* `update_atomtypes` returns, so on the failing path the saturated copy
still carried the unsaturated species' multiplicity beside zero radicals: `multiplicity 3` with no
radical electrons, which `from_adjacency_list` rejects. The message chose adjacency lists over
SMILES precisely so that rendering it could not fail the way the crash it replaces did — and then
printed a block that fails on re-read. Same instinct, one layer short. The handler now completes
the bookkeeping the raise interrupted, and the message says how to read the block: it parses with
`raise_atomtype_exception=False`, and the **only** obstacle otherwise is the `AtomTypeError` the
message already quotes. That last part is the honest end state rather than a workaround — the
saturated form of a metastable can never satisfy atom typing, because that is the whole content of
the failure, and the test asserts exactly that (`AtomTypeError`, never
`InvalidAdjacencyListError`).

**`qm/main.py` was the fifth call site and had been excused.** §18.2 said four adopt the helper and
the fifth is unreachable for a monatomic. True for argon, and beside the point: a cyclic
non-valence radical reaches it and receives the raw `AtomTypeError` the helper exists to replace.
Routed through the helper rather than defended in prose, which also makes "five call sites" true.

### 20.6 Checks run, and what each is relative to

Engine `i221-saturation-no-atomtype` at `18b94de25` (commits `14cca78b7`, `dee2954ef`,
`18b94de25` on `8ff42bd1a`), plasma head `40e21b495`; database at this commit.

| check | result |
|---|---|
| round-87 probe at `8ff42bd1a` | 8/8 findings reproduced, 4/4 controls hold |
| round-87 probe at `18b94de25` | 0/8 reproduced, 4/4 controls hold |
| new engine tests at `8ff42bd1a` | **7 failed**, 37 passed |
| `test/rmgpy/data` at `18b94de25` | **418 passed**, 8 skipped |
| `test/rmgpy/qm` at both | 8 failed either way — the same pre-existing failures (no MOPAC or Gaussian installed); the routed call site adds none |
| database `test/` on the pre-round-87 engine | **1 failed**, 323 passed — the new pin test, by design |
| database `test/` on `18b94de25` | **324 passed** |

Two qualifications on the red run, because a reader comparing counts will hit both.
`TestProvenanceNotTheFamilySlot` cannot be shown red that way at all: it imports
`authoring_family`, which the base does not define, so the module fails to import and the file
errors at collection rather than failing an assertion. The class was removed from the throwaway
copy so the rest could run, and the probe covers that half behaviourally instead. The eight
`ERROR`s in the same log are `setup_class` failures of the transport and solute classes in the
throwaway worktree, which has no configured database directory; the same classes pass in the real
one.

---

## 21. Round 90 — rebased onto the engine that ships the Chemkin writer

*The owner ruled on the rebase before it was done; the question and the four options are in the
session record. Nothing was pushed.*

### 21.1 Why it had to happen before the deck run

The plasma head moved from `40e21b495` to **`98d465d3b`** (Merge I-260, the one-range NASA writer)
while this branch sat on the old base. The file overlap is **zero** — upstream touched
`docs/contracts/i260-nasa-one-range.md`, `rmgpy/chemkin.pyx` and `test/rmgpy/chemkinTest.py`, and
this branch touches none of them and no `.pyx` at all — so a reader could reasonably have left the
branch where it was.

The reason not to: the staged deck exists to produce **an honest Chemkin export**, and I-260 *is*
the Chemkin writer. Running the deck on the pre-I-260 engine would have exported through the
routine that was just replaced, so a clean result would have been evidence about nothing anyone
will merge, and a dirty one could as easily have been I-260's.

### 21.2 The cost was much smaller than the round-89 handoff predicted

That handoff said the rebase "converts a five-minute verification into a full Cython build",
because the campaign's habit of copying the 52 `.so` files into a throwaway worktree breaks the
moment a `.pyx` changes upstream. That is true of the *throwaway-worktree shortcut* and false of
the worktree itself: the build tree here was intact (`build/temp`, `build/lib`, all 52 generated
`.c` present), so `make build` cythonized **exactly one file** and relinked it —

```
Compiling rmgpy/chemkin.pyx because it changed.
[1/1] Cythonizing rmgpy/chemkin.pyx
```

— in well under a minute, 104 `.so` before and after. Recorded because the same wrong estimate will
otherwise be repeated at the next upstream move: *ask whether the build tree survives* before
pricing a rebase as a rebuild.

Rebase safety, checked first: `git branch --contains 39336c8ab` named only the branch itself, the
worktree was clean with zero untracked files, and the pre-rebase tip is preserved as the tag
**`i221-pre-rebase-39336c8ab`**. All eight commits replayed with no conflict.

### 21.3 What was re-measured, and against what

Engine tip **`e0f075780`** on plasma head `98d465d3b`; database tip `9c88ea2b7`.

| check | result | relative to |
|---|---|---|
| round-89 delivery probe | **0 of 7 findings, 5 of 5 controls hold** | engine `e0f075780` |
| round-87 provenance probe | **0 of 8 findings, 4 of 4 controls hold** | engine `e0f075780` |
| engine `test/rmgpy/data` | **434 passed, 8 skipped, 0 failed** | engine `e0f075780` |
| engine `chemkinTest.py` + `electronPlacementTest.py` | **107 passed** — including all seven of I-260's one-range tests and the three plasma round-trip tests | engine `e0f075780` |
| database `test/` | **324 passed** | database `9c88ea2b7`, engine `e0f075780` |
| database `test/` on the **pristine** engine | **322 passed, 2 failed** — both by design | plasma head `98d465d3b` |

The `electronPlacementTest` figure is the one that matters for the round-89 addendum: the argon
ionisation channel still resolves through `FAMILY_ELECTRON_PLACEMENT` on the rebased engine, so
neither the rebase nor I-260 disturbed the second reader of `Reaction.family`.

### 21.4 Three count movements, each named rather than smoothed over

**(a) "1 failed by design" was stale; it is 2.** §19.1 and the pointer at the top of this report
both said a pristine engine gives 322 passed and 1 failed. Round 87 added a second negative control,
`test_this_runtime_ENFORCES_the_pin_as_more_than_an_attribute_lookup`, which fails on a pristine
engine for the same reason the first one does — so the figure has been 322/2 since round 87 and was
written down wrong at the moment it changed. Both are corrected above. The claim §19 rests on is
unaffected and slightly stronger: there are now two tests in the database's own suite that a
non-enforcing engine cannot pass.

**(b) The engine data suite reads 434, not round 89's 430.** Not drift: the round-89 run of that
suite predates commit `39336c8ab` (`e0f075780` after the rebase), which added exactly four tests —
the `TestTheFamilySlotIsLeftAloneForItsOtherReader` guard. The test code under `test/rmgpy/data` is
byte-identical across the rebase (`git diff 39336c8ab e0f075780 -- test/rmgpy/data rmgpy/data` is
empty), so nothing upstream could have moved it.

**(c) The first run of that suite reported 435 passed / 7 skipped and exited non-zero.** Two
separate artefacts of the *shared* checkout at `/home/alon/Code/RMG-database-plasma`, neither
belonging to this branch:

- `testSeed/` and `testSeed_edge/` had been left under `input/kinetics/libraries/` by an earlier
  `test/rmgpy/rmg/mainTest.py` run (not by this round — that file was never invoked here). The
  engine's pollution guard removed them and failed the run, which is the guard working. A clean
  re-run of the identical selection is **434 passed, 8 skipped, no pollution block, exit 0**.
- `Seed/` and `Seed_edge/` are **still there**, untracked, and the guard does not remove them
  because it only knows the `testSeed*` names. They are left in place: they are not this branch's
  to delete, and the standing rule is to preserve untracked files in checkouts that other sessions
  drive. Named here so the next reader of a collected-test count knows a shared checkout is part of
  the input.

### 21.5 What this round did not reach

The staged metastable deck at `/home/alon/runs/ar5torr-i261-20260922-125141/input.py` has still not
been run. The rebase was the precondition, and it is now met; the deck is the next step and the only
end-to-end evidence this branch has not yet produced.

Logs for everything above: `logs/round90-*` here, and `docs/i221-saturation/logs/round90-*` in the
engine worktree.

---

## 22. Round 90 — the deck ran, and the export is honest

The staged deck had been sitting unrun since round 80. It ran twice on the rebased engine
`e0f075780`. Run directories: `/home/alon/runs/ar5torr-i221-round90-20260922-222548` and
`…-nocantera-222701`; copies of both `RMG.log`/`stderr.log`, and the exported mechanism, are in
`logs/round90-deck-*`.

### 22.1 Before and after, on the same deck

The same deck was run at 12:51 today on the **pre-rebase** engine
(`/home/alon/runs/ar5torr-i261-20260922-125141`). It died here:

```
  File "rmgpy/chemkin.pyx", line 1715, in rmgpy.chemkin.write_thermo_entry
AssertionError
```

— the bare `assert len(thermo.polynomials) == 2` that I-260 replaced. Every species in this deck is
monatomic, so every one of them has a single NASA range, and the Chemkin writer refused all of
them without naming one. On the rebased engine that wall is gone: **model generation completes in
5 s** and the Chemkin files are written.

### 22.2 The metastable species survives the whole pipeline

`Ars` (`Ar u2 p3 c0`) reaches thermo, transport and the writer. Transport is the interesting one,
because it is the estimator this branch's engine half was built for. It does not crash; it falls
back, by name, with the reason:

> Estimating transport properties of Ars from the fallback Lennard-Jones parameters, because group
> additivity is not available for it: … replacing the species' 2 radical electron(s) with bonds to
> hydrogen gives a structure that no RMG atom type describes … This is expected for electronically
> excited species, such as a metastable noble gas, whose unpaired electrons are not unfilled
> valences. Supply transport data for this species directly in a library entry, or keep it out of
> the model.

That is the round-80 repair doing exactly what it was written to do, in a real run rather than a
test: an `AtomTypeError` many frames below the caller has become a sentence that names the species,
the cause, and the two ways out. (The `Error: Could not update atomtypes` line above it in `RMG.log`
is `update_atomtypes`' own logging on the way past and is not fatal.)

### 22.3 The export is right, not merely present

From `logs/round90-deck-chem_annotated.inp`, the two argon thermo blocks:

| species | library | a6 (H/R, K) |
|---|---|---|
| `Ar(2)` | `primaryThermoLibrary` | −745.375 |
| `Ars(4)` | `PlasmaExcitedNeutralThermo` | 133267.585 |

The gap the exported file therefore asserts between metastable and ground-state argon is

    (133267.585 + 745.375) K x R = 1114.246 kJ/mol = 11.5484 eV

against the NIST value for Ar(3P2), **11.5484 eV**. The number this branch put into the database
arrives at the other end of the pipeline intact, through a writer that had never emitted it before.
Both blocks are one-range NASAs split into two identical Chemkin ranges, which is exact for a
monatomic species — I-260's construction, exercised here on the species it was needed for.

The mechanism carries the two argon reactions with their electron-temperature declarations and
their honest annotations about what Chemkin cannot represent:

```
Ar(2)+e-(1)=>Arp(3)+e-(1)+e-(1)      2.981e+13 0.597  361.244
    TDEP/e-(1)/   ! ElectronCollisionPlasma exported as a modified-Arrhenius fit of k(Te) …
Arp(3)+e-(1)=>Ar(2)                  9.122e+13 -0.651   0.000
    TDEP/e-(1)/   ! TwoTemperaturePlasma reduced along T=Te; Ea_electron=0 J/mol is not representable …
```

`Ars` participates in no reaction: nothing in the loaded set has a metastable channel. It is in the
file as a species with correct thermo, which is what this branch claimed and all it claimed.

### 22.4 The next blocker, named and not fixed: the sibling writer

Both runs still exit **1**, and for one reason only. `rmgpy/yaml_cantera2.py:524-526` carries the
identical assumption I-260 removed from `chemkin.pyx`:

```python
'temperature-ranges': [sorted_polys[0].Tmin.value_si, sorted_polys[0].Tmax.value_si,
                       sorted_polys[1].Tmax.value_si],
'data': [polys[0]['data'], polys[1]['data']]
```

A one-range NASA gives `IndexError: list index out of range` — and, exactly as before the I-260
repair, the failure names no species. Cantera's own NASA7 model accepts a single range, so this
writer is stricter than the format it targets.

**It cannot be worked around from the deck.** Setting `generateCanteraYAML2=False` was tried in the
second run and is refused by design:

> No Cantera artifact was produced for this plasma mechanism. The Chemkin-to-Cantera translation
> cannot represent its electron-temperature rate laws (TDEP/ lines, which ck2yaml rejects), and the
> only writer that can represent them — the direct cantera2 writer — is disabled.

That guard is correct and should stay. The consequence is that **every plasma deck containing a
monatomic species cannot produce a Cantera artifact today**, which is a larger blast radius than
this ticket and belongs to whoever owns I-260's family of writers. Named here per the standing
rule; not fixed, because `rmgpy/yaml_cantera2.py` is not this ticket's file.

### 22.5 What this settles and what it does not

Settled: the claim that this branch is the last blocker on an honest Chemkin export is now
demonstrated rather than argued — the export exists, and its numbers are right.

Not settled: the run still ends non-zero, so "a clean end-to-end plasma run" remains unreached, on
a defect that is not this branch's. The deck also substitutes `terminationTime = 1e-3 s` for
"quasi-steady state" (the deck's own note 2), so nothing here is a statement about the steady state.

---

## 23. For the next review round: what round 90 claims, and where to push

The owner's ruling after §22 was to hold the branches for another adversarial round rather than
push. This section exists to make that round cheap: every load-bearing claim of round 90, how it
was measured, and the places I would attack first.

### 23.1 The claims and their measurements

| claim | how it was measured | named against |
|---|---|---|
| The rebase changed no behaviour | both probes re-run green; `git diff 39336c8ab e0f075780 -- test/rmgpy/data rmgpy/data` empty | engine `e0f075780` |
| The second reader of `Reaction.family` is intact | `electronPlacementTest.py` in the 107-passed run | engine `e0f075780` |
| A pristine engine fails exactly the two negative controls | database `test/` with `PYTHONPATH` at `/home/alon/Code/RMG-Py-plasma` | plasma head `98d465d3b` |
| The deck's Chemkin export carries the right excitation energy | a6 difference in the emitted file | `logs/round90-deck-chem_annotated.inp` |
| The remaining failure is not this branch's | traceback at `yaml_cantera2.py:525` in both runs | engine `e0f075780` |

### 23.2 Where I would push, if I were reviewing this

**The excitation-energy check is narrower than it looks.** The a6 difference equals ΔH only because
both species are monatomic with identical `a1 = 2.5`, so the gap is temperature-independent; I
checked that condition holds in the emitted file, but the identity would not survive a species with
real heat capacity. And it verifies the *export path* — that the library number reaches Chemkin
undistorted — not the entry itself, which rounds ≤58 settled separately. It is a strong check of
exactly one link.

**The deck's own header is stale, and I did not repair it.** Note 3 of `input.py` says 3 eV typed as
34813.5 K, while the reactor block passes `electronTemperature=(10442.0, 'K')` = 0.8998 eV, with its
own comment calling that the measured ionisation/wall-loss balance point. The runs used 0.900 eV.
The prose and the code disagree by a factor of 3.3 in Te, and the prose is the wrong one. The deck
is not a repository file and is not this ticket's, so it was left alone and is named here instead.

**`Ars` participates in no reaction.** Nothing in the loaded set has a metastable channel, so the
run exercises thermo, transport and the writer for that species and no kinetics at all. "The
pipeline works" should be read with that scope.

**The model is tiny and the termination is a substitute.** Four core species, two to three
reactions, 5 s of execution, and `terminationTime = 1e-3 s` standing in for "quasi-steady state"
(the deck's own note 2). Nothing here is a statement about a steady state.

**The pristine-engine control depends on somebody else's build.** It ran against
`/home/alon/Code/RMG-Py-plasma`, which I did not rebuild. Checked rather than assumed: that
worktree's `chemkin` `.so` is dated 13:11 against a `.pyx` of 13:10 and a HEAD commit of 13:10:36,
so it is a current build of `98d465d3b`.

**What I could not reach.** A clean end-to-end plasma run — blocked on §22.4, which is not fixable
from inside this ticket. `test_make_profile_graph` remains unreached for the separate reason named
in round 89 (no graphviz `dot` installed). And the `Seed/` and `Seed_edge/` directories left
untracked in the shared `/home/alon/Code/RMG-database-plasma` checkout are still there, still not
mine to delete, and still part of what the engine suite collects against.
