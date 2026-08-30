# I-179 — Fork-C re-verification of the argon cation thermochemistry, and the deck gap it exposed

**Headline.** I-179 was scoped to *source* argon cation thermochemistry on the premise that none
existed. That premise was false: commit `2d7123b08` (I-127), already an ancestor of this branch,
had entered a sourced `Ar⁺` value. The manager withdrew the original Verifier and reshaped the work
to **fork C**: re-verify I-127's `Ar⁺` independently on the runtime the campaign is about to depend
on (`RMG-Py-i172-balance`, `ed2ee5901`), treating it as a value we will build a simulation on, not
a formality. **The values, provenance, and ion convention all hold. The new finding is not about
the entry — it is that the canonical plasma deck does not load the library that carries it, so as
the deck stands `Ar⁺` is still refused at the thermochemistry wall.** No new thermo values were
entered. One piece of library prose was corrected (it wrongly said the dication cannot be built).

## 1. What was verified, and the evidence

Runtime pinned to `/home/alon/Code/RMG-Py-i172-balance` (`ed2ee5901`, 104 `.so`); database pinned to
this worktree. The verifier is the fork-C probe (19/19 PASS) plus a new committed regression test
`test/test_argon_cation_buildtime.py` (5/5 PASS). Numbers are re-derived, not copied from I-127.

### 1.1 Values transcribe NIST-JANAF Ar-002 (stored entry, verbatim)

| quantity | entered | source (NIST-JANAF Ar-002 / derived) | check |
|---|---|---|---|
| H298 (kJ/mol, ion convention) | 1520.581 | 1526.778 (EC) − 6.197 = 1520.581 | exact |
| S298 (J/mol·K) | 166.404 | S(Ar) 154.845 + R ln 4 + 0.033 electronic = 166.404 | exact |
| E0 (kJ/mol, 0 K) | 1520.573 | JANAF Ar-002, T=0 row | exact |
| Cp(T), 13 pts 298–6000 K | JANAF Ar-002 column | — | worst dev 0.0000 |
| validity range | 298.15–6000 K | JANAF table span; `Tmax`=6000 K | stated |

### 1.2 Ion convention (the easy thing to get wrong) — the free electron is *in* the reference state at zero

The database prices the free electron at zero enthalpy/entropy/Cp at all T (the **ion convention**),
so a cation's ΔfH° does **not** include the released electron's thermal energy. Verified three ways:

- **All three `electron` entries** in the 78 loaded libraries return H=S=Cp=0 at every T.
- **Two independent reconciliation routes** from JANAF's electron-convention value close to
  0.0014 kJ/mol: `1526.778 − 5/2 R T = 1520.5806` and `1520.573 + 6.206 − 6.197 = 1520.582`.
- **E0 equals argon's first ionisation energy** from an unrelated database (NIST ASD,
  15.7596119 eV = 1520.5714 kJ/mol) to 0.0016 kJ/mol.

The entry follows the same convention as the existing `[Lip]`, `Li_ion`, `proton` and `electron`
entries — evidenced by every DB electron entry being an all-zero NASA polynomial. **This is the
convention check Verifier 3 asked for.**

### 1.3 Build-time resolution — the crux, and the finding

`get_thermo_data` is the exact method RMG's model builder calls; the only thing separating a
"direct query" from "build time" is *which libraries are loaded*. At build time that set is the
input deck's `thermoLibraries`.

- With `PlasmaCationThermo` among the loaded libraries, the library **wins** over group additivity:
  `get_thermo_data(Ar⁺)` returns `Thermo library: PlasmaCationThermo`, H298 = 1520.584 kJ/mol
  (the ~3 J/mol Wilhoit round-trip off the stored 1520.581).
- With the **canonical plasma deck's** `thermoLibraries` — transcribed verbatim from
  `RMG-Py/docs/i123-integration/input.py`:
  `['LithiumPrimaryThermo', 'LithiumAdditionalThermo', 'primaryThermoLibrary', 'electrocatThermo']`
  — `Ar⁺` is **refused with a loud `DatabaseError`**, because the library is not loaded and group
  additivity fails loudly for the noble-gas cation. It is **not** handed a silently fabricated
  number.

**→ CRITICAL-PATH FINDING for the project owner.** The `Ar⁺` entry is correct and does win at build
time *when the deck loads the library*. The reference plasma deck does not. **An argon-capable deck
must add `PlasmaCationThermo` to its `thermoLibraries`.** That one-line deck change lives in the
RMG-Py runtime repo (`docs/i123-integration/input.py`), not this database, so it is reported here and
not made from this worktree.

### 1.4 "Loud failure, not silent fabrication" — which `Ar2+` is which

Both species written "Ar2+" in ASCII build, and **both raise a loud `DatabaseError` — neither is
silently fabricated**:

| species | reading | adjacency list | builds? | thermo query |
|---|---|---|---|---|
| **Ar(2+)** | dication, monatomic +2 | `1 Ar u2 p2 c+2` (³P) | YES, net +2 | loud `DatabaseError`, "no data … for atom **Ar++**" |
| **Ar2(+)** | dimer cation, diatomic +1 | `1 Ar u0 p3 c+1 {2,S} / 2 Ar u1 p3 c0` | YES, net +1 | loud `DatabaseError` (HBI saturation → `[Ar+][ArH]`) |

The **dication `Ar(2+)`** is the one the contract's "species construction is not the barrier" refers
to. The campaign's danger thesis ("missing thermo → silent group-additivity number") **does not
apply to any argon cation**: argon is the noble-gas case where group additivity fails loudly. The
silent-fabrication risk is real only for non-noble monatomic cations (e.g. Li⁺); see I-127 §4.

## 2. The library prose fix

`input/thermo/libraries/PlasmaCationThermo.py` "WHAT IS NOT HERE" claimed *"RMG cannot construct a
doubly charged monatomic cation, so there is nothing for a thermochemistry entry to attach to."*
That is **wrong** — the dication builds (§1.4). It also used the identical string "Ar2+" for two
different species (dimer at one point, dication at another), which is exactly the ambiguity that
made the original I-179 ticket unanswerable.

The section was rewritten to (a) disambiguate `Ar2(+)` dimer vs `Ar(2+)` dication explicitly, and
(b) state the real reason the dication has no entry: it *builds*, there is no NIST-JANAF table above
Ar-002, and a thermo query raises a loud `DatabaseError` rather than fabricating a number — so there
is nothing to source, not nothing to attach to. Docstring-only change; asserted by no test; the
library re-parses and re-loads cleanly.

## 3. Science queue — for the project owner (do not chase from here)

**`Ar2(+)` argon dimer cation thermochemistry is unsourceable from this environment, and here is
exactly what is missing.** It is wanted: I-120 measured Ar₂⁺ dissociative recombination ~2.9×10⁵×
faster than Ar⁺ radiative recombination at Te = 1 eV, making it the dominant argon electron sink.

- The tabulated functions exist: **Maltsev, Morozov & Osina, "Thermodynamic Properties of Ar2+ and
  Ar2 Argon Dimers", *High Temperature* 57 (2019) 37–40, doi:10.1134/S0018151X19010176**, covering
  298.15–10000 K, folded into IVTANTHERMO.
- Blockers from here: Springer paywalled (303→IdP); OpenAlex `W2964635563` `oa_status: closed`;
  ATcT argon-dimer-cation page (species 2778) HTTP 403; NIST WebBook `Ar2` carries only the neutral
  dimer's ion energetics, no gas-phase thermo; **no NIST-JANAF Ar₂⁺ table** (argon tables stop at
  Ar-002).
- **What unblocks it:** the Maltsev tables via institutional Springer access or a library request —
  the owner has literature access this environment lacks. With Cp(T) and S(298) in hand the entry is
  a transcription, same shape as the `Ar⁺` entry. Deriving it from `D₀(Ar₂⁺)` is forbidden authoring
  and would still leave S° and Cp(T) unsourced.

## 4. Other things noticed — reported, not fixed

- **Runtime drift in the atom-type registry.** Running I-127's `test/test_argon_cation_thermo.py` on
  `i172-balance` yields **5 failures, all non-argon**: `Na⁺`, `Mg⁺`, `K⁺`, `Ca⁺` no longer raise
  `KeyError` (the balance runtime added charged atom types for them; I-127's test pinned the
  `i123-integration` behaviour where they had none), and `test_argon_is_representable_only_because_…`
  fails for the same reason (the representable-set changed). The **argon** value, convention, and
  resolution tests all pass. This is stale test expectation vs. a more permissive runtime, not an
  argon regression. Left as-is (updating it is another ticket's scope).
- **Ten multiply-charged cations remain thermo-less** (He²⁺, Ne²⁺⁻⁴⁺, Si²⁺⁻⁴⁺, Ar²⁺⁻⁴⁺): they
  build (charge-unconstrained atom types) but have no sourced thermo and fail loudly. Not in scope.

## 5. Verifier results

| # | check | result |
|---|---|---|
| 1 | before-state measured, premise inverted (Ar⁺ already entered & resolving) | PASS (reported to manager) |
| 2 | every value has citation + temperature range | PASS — §1.1 (no *new* values entered) |
| 3 | ion-convention determined with evidence from existing entries | PASS — §1.2 |
| 4 | DB returns sourced value, not GA, at build time when library is loaded | PASS — §1.3 |
| — | fork-C probe | 19/19 PASS |
| — | `test/test_argon_cation_buildtime.py` (new) | 5/5 PASS |
| — | `test/test_argon_cation_thermo.py` on i172-balance | 43 pass / 5 fail (non-argon drift, §4) |
| — | full `databaseTest.py` | not run — change is docstring-only; library re-loads cleanly; `test_thermo` validates group trees, not library prose |
