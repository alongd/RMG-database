# I-234 — Argon radiative recombination: sourced, entered, and it is not negligible

**The most important finding is not about argon.** Adding this entry silently disabled twenty
existing checks on the lithium entry that was already there — not by breaking an assertion, but by
expiring a fixture precondition, which pytest reports as a setup *error* rather than a failure, so
the checks stopped running while the suite still printed green for the rest. That is §0, and it is
a cleaner instance of this campaign's own subject than anything else here. Fixed; 47 → 69 passing,
zero errors.

**On argon, the result inverts the brief.** The brief anticipated that a correctly sourced rate
would turn out to be negligible at 5 torr / 3 eV, and asked for the comparison that would establish
it. The comparison says the opposite: **this entry is the only loss channel in the mechanism, so it
alone sets the end state.** Without it argon ionises until the neutral is gone; with it the model
settles at a heavy-species neutral fraction of `1.213e-3`, which is `alpha/k_iz`. The channel is
determinative here for a reason that is itself a finding and not a flattering one (§6.4).

Three further contradictions of the framing, all measured:

- **My own first estimate was wrong, and the run caught it.** Evaluated at the deck's seed state
  the RR sink is `7.5e-11` of the ionisation source and the RR timescale is ~600 s against a
  1e-3 s run — apparently inert by ten orders of magnitude. That arithmetic is correct and
  answers the wrong question, because the system leaves that state within a microsecond (§6.1).
- **I-120 ruled this rate must not be entered. All three of its supports have since moved** (§7).
- **Neither available source publishes an uncertainty, and none is offered** (§3.4). An earlier
  draft advised using the inter-fit spread as an error bar; that is withdrawn.

---

## 0. The finding this ticket is really about: a precondition that expired and took twenty checks with it

Adding correct, sourced data to this library **silently disabled twenty existing checks on the entry
that was already there.** This is a cleaner instance of the campaign's own subject — a justification
that goes stale without anyone touching it — than anything else in this report, so it goes first.

```
base 20cfc36cc,  test_plasma_radiative_recombination.py + test_plasma_argon.py   47 passed
850c81cf0,       same two files, same command                    3 failed, 20 errors, 24 passed
```

**Nobody wrote a bad assertion.** The fixture at `test_plasma_radiative_recombination.py:134` read:

```python
@pytest.fixture
def reaction(library):
    reactions = library.get_library_reactions()
    assert len(reactions) == 1          # <- the precondition
    return reactions[0]                 # <- selection by position
```

That encodes *"this library has exactly one entry"* as a **precondition of twenty tests** rather
than as a **claim made by one**. The moment the library grew, the precondition expired.

**Why that is worse than a failure, and the reason it is worth a section.** The twenty did not
fail — they **errored in setup**. Pytest reports a setup error as an error, not a failure, and an
errored test asserts nothing. So the suite quietly stopped checking twenty properties of the
*lithium* entry — its electron propagation, its balance, its placement resolution, its reactor
acceptance — none of which the argon entry had any bearing on, and still printed a green count for
the 24 that remained. **A failure argues with you; a setup error just removes the check and leaves
a smaller green number behind.** A reader skimming for red sees three failures about entry counts,
fixes those, and ships a suite twenty assertions weaker than the one they started with.

**The fix, and the rule it encodes.** Selection is now by identity, not position:

```python
def _reaction_for(library, reactant_label): ...   # asserts exactly one match for THAT label
@pytest.fixture
def reaction(library):        return _reaction_for(library, '[Lip]')
@pytest.fixture
def argon_reaction(library):  return _reaction_for(library, '[Arp]')
```

The library's size is now asserted in exactly **one** place — `test_library_loads_with_the_expected_coverage`
— where it is a claim that fails loudly and in isolation, and where it pins *what* is covered rather
than merely *how many*, so a wrong second entry cannot satisfy it. Two other tests were carrying the
same precondition for their own reasons and were corrected the same way: the three-body tripwire now
loops over every entry (strictly stronger than insisting there is one), and the coverage test names
`{Li+, Ar+}`.

**Result:**

| | base `20cfc36cc` | after the fix |
|---|---|---|
| passed | 47 | **69** |
| failed | 0 | 0 |
| errors | 0 | 0 |

All 46 unchanged base tests still run, one was deliberately renamed
(`test_library_loads_with_exactly_one_entry` → `..._with_the_expected_coverage`), and **22 new argon
tests** were added at the same strength as the lithium ones — mirroring them rather than sampling
them, because the argon entry differs in three ways that each defeat a lithium-shaped check: a
different kinetics class, a transcribed rather than table-loaded coefficient, and a two-temperature
evaluator instead of an electron-temperature one. Verified by diffing collected test ids against the
base commit.

### 0.1 The same trap is still armed in two sibling files — measured, not fixed

Having found the pattern, I searched for it. It is not unique to this file:

```
test/test_plasma_electron_impact_ionization.py:112-116   @pytest.fixture def reaction(library):
                                                             reactions = library.get_library_reactions()
                                                             assert len(reactions) == 1
test/test_plasma_argon.py:61-65                          identical
```

Both are byte-for-byte the construct that just cost twenty checks, in the fixtures for
`PlasmaElectronImpactIonization` (one entry, lithium) and `PlasmaArgon` (one entry, argon
ionisation). Each also has a `test_library_loads_with_exactly_one_entry` asserting the count.
**The day either library gains a second entry, the same silent disabling happens to that file** —
and both are libraries this campaign is actively expanding, so this is a live hazard rather than a
theoretical one.

**Not fixed here, deliberately.** Both libraries have exactly one entry today, so the corrected
fixture would be a no-op with no failing test to demonstrate it works, and changing tests you
cannot exercise is its own risk. The fix pattern is proven in this file against a genuinely
two-entry library and transfers mechanically. Flagged for its own ticket rather than folded in
silently.

---

## 1. The three entry counts, re-run as my own numbers

Re-counted before trusting the brief. All three agree with it.

```
input/kinetics/libraries/PlasmaRadiativeRecombination/reactions.py    -> 1 entry:  [Lip] => [Li]
input/kinetics/libraries/PlasmaElectronImpactIonization/reactions.py  -> 1 entry:  [Li]  => [Lip]
input/kinetics/libraries/PlasmaArgon/reactions.py                     -> 1 entry:  Ar + e- => Arp + e- + e-
```

The 5 torr deck's core, as generated, is **3 species and 1 reaction** — also as the brief stated,
and confirmed by running it (§5).

---

## 2. Does the family admit an argon cation? No — measured, not assumed

`Plasma_Radiative_Recombination` roots its template on

```
1 *1 R u0 px c[0,+1,+2,+3,+4,+5,+6,+7,+8]
```

Matched against molecules built from adjacency lists (never SMILES — this database's monatomic-ion
SMILES round trip is known to corrupt charge):

| species | adjacency list | `is_subgraph_isomorphic(root)` |
|---|---|---|
| Ar⁺ | `1 Ar u1 p3 c+1` | **False** |
| Ar  | `1 Ar u0 p4 c0`  | True |
| Li⁺ | `1 Li u0 p0 c+1` | True |

**The root demands `u0` and refuses Ar⁺ outright**, because argon's cation ground state is
3s² 3p⁵ — one unpaired electron, `u1`. The family's recipe is also the wrong direction for argon:
`GAIN_RADICAL` takes u0 → u1, whereas argon's recombination takes u1 → u0. The library, which has
no template, is therefore the only possible owner for this reaction — which is what was built.

**The second half of the defect is the more dangerous one and is easy to miss.** The root does
*not* refuse neutral argon; it matches it. Applying the family's recipe
(`GAIN_RADICAL(*1,1)` + `LOSE_CHARGE(*1,1)`) to `1 Ar u0 p4 c0` gives `1 Ar u1 p4 c-1`, and RMG
cannot construct that species at all:

```
AtomTypeError: Unable to determine atom type for atom Ar.-, which has ... 4 lone pairs, and -1 charge
```

So the family is not merely unable to help argon; loaded against an argon deck it would reach for
an argon anion that does not exist in RMG's type system. This is latent rather than live today —
the 5 torr deck lists only `Plasma_Electron_Attachment` under `kineticsFamilies` — but it is a
crash in waiting for any deck that does load this family alongside argon.

**Both halves are filed as I-236** (families-and-data milestone, argon lane). Per the owner's
decision this ticket reports and does not work around: no family file is touched.

---

## 3. Sourcing the rate

### 3.1 Why the obvious table cannot supply argon

`input/kinetics/badnell.yaml` holds **33 nuclear charges and 318 (Z, N) stages**, Z ∈ {1–30, 36,
42, 54}. `Z: 18` *is* present — which briefly looked like it contradicted the
`PlasmaRadiativeRecombination` longDesc — but its stages run **N = 0…11 only**, and Ar⁺ needs
N = 17. Enumerating the cation-to-neutral stages (`N = Z − 1`) across the whole table gives
exactly **Z = 1…12**. The library's prose is accurate and my initial suspicion of it was wrong;
recorded because the near-miss is the kind that gets re-litigated. The structural reason is that
Badnell (2006) runs isoelectronic sequences H-like through Na-like, and Ar⁺ is Cl-like.

### 3.2 What was entered

**[ShullVanSteenberg1982]** J. M. Shull and M. Van Steenberg, "The Ionization Equilibrium of
Astrophysically Abundant Elements", *Astrophys. J. Suppl. Ser.* **48** (1982) 95–107.

Their equation (4) is `alpha_r(T) = A_rad * (T / 10^4 K)^(-X_rad)` [cm³/s], and Table 2 row `AR1`
carries, for argon:

```
A_rad = 3.77E-13        X_rad = 6.51E-01
```

Both transcribed verbatim from that row, read out of the ADS scan's OCR text layer directly rather
than taken from a secondary. `A` is written into the entry in the paper's own units
(`cm^3/(molecule*s)`) so that RMG performs the unit conversion and **no arithmetic is done by
hand**; `n = -0.651` is `-X_rad`; `T0 = 1e4 K` is the paper's own normalisation.

**Which row, and why it is the right one.** Table 2's own footnote says so outright:

> "Rates refer to collisional ionization of and recombination to the tabulated ion."

So row `X_n` carries recombination *to* stage `X_n`, and `AR1` is the reaction yielding neutral
Ar I, i.e. `Ar+ + e- => Ar`. I originally proved this the hard way, by internal consistency — for
every element the last row (C6, N7, O8, NE10, MG12, SI14, S16) carries `X_rad = 7.26E-01` with a
null dielectronic entry, the hydrogenic value, which only the bare nucleus recombining to the
H-like ion can be. That argument is sound and was unnecessary; the footnote is the direct proof
and is now what the entry cites, with the consistency check and Verner's `rrfit.f` encoding
(`A = 3.770e-13, B = 0.6510` at `IN = 18`) kept as corroboration rather than as the argument.

The provenance chain is corroborated by an open, readable, peer-reviewed third party —
Mazzotta et al. 1998, A&AS 133, 403 (arXiv astro-ph/9806391), §2.2:

> "For the radiative recombination rates the calculations of Shull and Van Steenberg (1982)
> (hereafter SV) were used for some of the most abundant astrophysical elements (Mg, Si, S, **Ar**,
> Ca, Fe, Ni). They give the fitting parameters A and η for the following formula:
> αr = A (T/10⁴ K)^η [cm³/s], with the **electron temperature** T …"

### 3.3 The validity range, stated as exactly what it is

**Shull & Van Steenberg declare no numerical validity range for the fits.** They say only that
they "attempted to simplify the rate coefficients with analytic fits over the temperature range of
interest" (§II), and never name that range where the recombination fits are given (§II(b)).

`Tmin = 1e4 K` / `Tmax = 1e8 K` in the entry are therefore **grid membership and nothing more** —
not a quoted bound, and specifically **not a demonstrated accuracy bound for this fit**. They are
the span over which the authors exercise these rates: Table 3 tabulates argon ionisation fractions
at `log T = 4.00` through `8.00`, and §III states those results "are applicable to any hot,
optically thin, low density plasma in ionization equilibrium." That the authors ran the fit over
that span is evidence they considered it usable there; it is not an error bound, and neither the
entry nor this report should be read as offering one. **No accuracy bound for this fit is available
from any source consulted.**

The deck runs at `Te = 34813.5 K`, inside that span. The two entries in this library do not share a
floor: the Li⁺ `BadnellRRArrhenius` is valid down to 10 K, this one is not.

**And nothing enforces either number — measured.** No evaluation path consults them.
`is_temperature_valid(298.15)` returns `False` while `get_rate_coefficient_two_temp` returns an
ordinary number at `Te = 0.5 eV` (5802 K, below `Tmin`), with no warning and no raise:
`5.373287e-13 cm³/s` delivered from outside the declared range. So `Tmin`/`Tmax` are documentation
for a reader, not a guard against a caller. Pinned by
`test_the_declared_temperature_range_is_grid_membership_that_nothing_enforces`. **Referred, not
fixed** — making the engine enforce a declared range is an RMG-Py change and out of scope here.

### 3.4 Uncertainty: there is none to quote, and that is the finding

**Neither candidate source states an uncertainty, so no error bar is offered.** An absent quantity
is reported absent.

> **Correction, and it is mine to carry even though the instruction was not.** An earlier draft of
> this report and of the entry advised a reader who needs an error bar to use the ~48 % spread
> below as one. That was wrong. Two fits that share an ancestor disagreeing by 48 % is neither an
> uncertainty interval nor a lower bound on the error — it is a comparison between two particular
> calculations, and telling a reader to use it as an error bar asserts something the evidence does
> not support. The advice is withdrawn from both. The spread is still reported, as a spread.

What follows is a comparison between this fit and the one rival fit for the same reaction. Both
values are transcribed from their sources.

The rival is CHIANTI `ar_2.rrparams` — six-parameter Badnell/Gu form (A = 4.6460e-11 cm³/s,
B = 0.67040, T0 = 7.4230 K, T1 = 5.2750e6 K, C = 0.38320, T2 = 3.9120e4 K), refitted for CHIANTI
in 2008 by P. R. Young and K. P. Dere from Aldrovandi & Péquignot, *Rev. Bras. Fis.* **4** (1974)
491, procedure in Dere et al., A&A 498 (2009) 915 §3.

| Te | SVS82 α (cm³/s) | CHIANTI/AP74 α (cm³/s) | ratio |
|---|---|---|---|
| 0.3 eV | 7.493e-13 | 7.352e-13 | 0.98× |
| 0.5 eV | 5.373e-13 | 5.197e-13 | 0.97× |
| 1.0 eV | 3.422e-13 | 3.371e-13 | 0.99× |
| **3.0 eV** | **1.674e-13** | **2.472e-13** | **1.48×** |
| 5.0 eV | 1.200e-13 | 2.386e-13 | 1.99× |

Two facts about the pair, recorded as facts and not as a bound:

- **The two fits are not independent at the root** — both descend from Aldrovandi & Péquignot
  (SVS82 §II(b) cites AP 1973, 1976 as its radiative source). This is exactly why their difference
  is uninformative about the error of either: common ancestry means their agreement is partly
  inherited and their disagreement measures divergence between parameterisations, not distance
  from the truth.
- **The spread is strongly Te-dependent, and worst where this deck runs.** The two agree to 1–3 %
  at 0.3–1 eV and diverge above it, because the Gu form's `C*exp(-T2/Te)` term flattens the high-Te
  falloff while the single power law keeps falling. I-120 compared these two at 1 eV and found them
  1.5 % apart; that agreement does not survive to 3 eV. Useful when choosing between them; still
  not an error bar.

**The disclosure that must travel with this number.** SVS82 §II(b) states the radiative
coefficients came from AP for C, N, O, Ne, Mg, Si and S, and then: *"Values for Ar, Ca, and Ni are
derived by interpolating along isosequences."* Their conclusion asks for precisely the check argon
still lacks: *"Future experimental cross sections or theoretical calculations of these rates for
elements with Z > 10 would be valuable in checking the validity of our isoelectronic
extrapolations."* Argon is Z = 18. This is the compilers' own interpolation, disclosed in their
paper and quoted verbatim in the entry — not an interpolation performed by this database — but a
reader must know it is there. It is the reason this entry and its rival each fail a different
clause of the ticket's sourcing rule, which is why the choice between them was escalated rather
than made silently.

---

## 4. The temperature the rate reads — verified, not asserted

This was a hard requirement, and in a two-temperature system it is the difference between a
correct entry and a silently wrong one. It was checked at both levels.

**Level 1 — the class.** `TwoTemperaturePlasma` computes
`k(T,Te) = A*(Te/T0)^n * exp(-Ea_g/RT) * exp(Ea_e(Te-T)/(R·T·Te))`. With `Ea_g = Ea_e = 0` this
collapses to `A*(Te/T0)^n` — **exactly** SVS82 equation (4), an exact representation rather than an
approximation, driven by Te alone.

**Level 2 — the runtime dispatch.** This is the part that actually decides it.
`PlasmaReactor.evaluate_two_temperature_rate_coefficient` (`rmgpy/solver/plasma.pyx:837-847`)
routes every `uses_electron_temperature` object to `get_rate_coefficient_two_temp(T, Te)`, and its
docstring records that the ordinary interface *"is deliberately never used for these kinetics: it
collapses to a one-temperature evaluation (k(T, Te=T))."* The entry's class sets
`uses_electron_temperature = True` and exposes that evaluator, so it is routed correctly.

**The check, at the deck's conditions (Tgas = 298.15 K, Te = 34813.5 K):**

```
two-temperature evaluator   k = 1.007893e+05 m^3/(mol*s)   alpha = 1.6736e-13 cm^3/s   <- used
gas-temperature collapse    k = 2.234783e+06 m^3/(mol*s)   alpha = 3.7109e-12 cm^3/s
ratio                       22.173x

hand-check on Te:  3.77e-13*(34813.5/1e4)**-0.651 = 1.673646e-13 cm^3/s   <- matches
hand-check on T :  3.77e-13*(298.15/1e4)**-0.651  = 3.710943e-12 cm^3/s
```

**Reading the gas temperature here would give a rate 22.2× too high.** It does not.

**The Chemkin export is also faithful, and that was not guaranteed.** The written reaction is
`Arp(3)+e-(1)=>Ar(2)  9.122e+13  -0.651  0.000` carrying `TDEP/e-(1)/`, with the comment
"TwoTemperaturePlasma reduced along T=Te; Ea_electron=0 J/mol is not representable in Chemkin and
is dropped". Because this entry sets `Ea_e = 0`, the dropped term is zero and **the reduction is
lossless for this entry specifically** — it would not be for an entry with a non-zero electron
activation energy. The A-factor reconciles exactly:
`2.27035e11 cm³/(mol·s) × (1e-4)^(-0.651) = 9.122e13`.

---

## 5. The deck, run both ways

All four runs exit 0. Both streams captured for every run, in `logs/` — with one blemish worth
naming rather than hiding: for the `prof-without` run my redirection merged stderr into the stdout
log, so `prof-without.stderr.log` is empty and `prof-without.stdout.log` carries both. Nothing was
lost (the 29 warning lines that appear in the sibling runs' `stderr.log` are present there), but an
empty `stderr.log` should not be read as "this run printed nothing to stderr". The other three runs
have cleanly separated streams.

| | core species | core reactions | edge species | edge reactions |
|---|---|---|---|---|
| **without** the entry | 3 | **1** | 2 | 2 |
| **with** the entry | 3 | **2** | 2 | 2 |

The entry adds exactly one core reaction and no species. The two edge species are `[Li](4)` and
`[Lip](5)`, pulled in by the lithium entries of the two plasma libraries the deck loads; they never
reach the core, as expected in an argon-only mixture.

### 5.1 The two arms are NOT reproducible from the committed files, and here is what to do

This needs stating plainly because the committed evidence does not show it. **The two profile decks
(`prof-with/input.py`, `prof-without/input.py`) are byte-identical.** Both resolve the database
through an `rmgrc` pointing at this checkout, and `rmgrc` is `.gitignore`d by deliberate project
policy — a tracked one pins a checkout-specific path and has previously produced
meaningless-green runs. So re-running `prof-without/input.py` **today reproduces the *with* arm**,
because the library in this checkout now contains the argon entry.

The distinction between the arms lived entirely in a database state that no committed file carries:

- `run-without/` and `prof-without/` were run with `input/kinetics/libraries/PlasmaRadiativeRecombination/`
  at commit `20cfc36cc` (one entry, lithium only);
- `run-with/` and `prof-with/` were run with it at `850c81cf0` (two entries).

**To reproduce the *without* arm by hand:**

```bash
git checkout 20cfc36cc -- input/kinetics/libraries/PlasmaRadiativeRecombination/
printf 'database.directory = %s/input\n' "$PWD" > docs/argon-radiative-recombination/prof-without/rmgrc
cd docs/argon-radiative-recombination/prof-without && \
  PYTHONPATH=/home/alon/Code/RMG-Py-plasma python /home/alon/Code/RMG-Py-plasma/rmg.py input.py \
  > >(tee -a ../logs/prof-without.stdout.log) 2> >(tee -a ../logs/prof-without.stderr.log >&2)
cd - && git checkout HEAD -- input/kinetics/libraries/PlasmaRadiativeRecombination/
```

That is what was actually done — the library was reverted with `git checkout`, the matched run
performed, and the edited files restored from a backup **verified byte-exact by md5** afterwards.
The committed files cannot carry it because the arm is selected by database content rather than by
anything in the deck, and the one file that would pin the database path is correctly untracked.

A deck-level switch would be better than a procedure in prose — the `without` arm is really "load
this library minus one entry", which no input directive can express. Recorded as a limitation of
this comparison rather than fixed here.

---

## 6. Does it matter? Yes — and this is where the brief's expectation fails

### 6.1 The seed-state estimate, which is correct and answers the wrong question

At the deck's initial condition — `n_Ar = 1.6194e23 m⁻³`, `n_e = 1e16 m⁻³`, ionisation fraction
`6.18e-08`, `k_iz(3 eV) = 1.3781e-10 cm³/s` integrated from the shipped `PlasmaArgon`
cross-section table:

```
ionisation source  S = k_iz n_e n_Ar    = 2.2317e+23 m^-3 s^-1
RR sink            L = alpha n_e n_Ar+  = 1.6736e+13 m^-3 s^-1
L/S                                     = 7.4992e-11
RR timescale for one Ar+ ion: 1/(alpha n_e) = 597.5 s   (run ends at 1e-3 s)
```

Ten orders of magnitude below the source; a timescale six hundred thousand times the whole
simulation. On this alone the entry is inert, and this is the estimate I carried into the runs.
**The run refuted it.** The failure is that both rates are evaluated at a state the system
abandons within a microsecond: the RR sink scales as `n_e·n_Ar+` while the source scales as
`n_e·n_Ar`, so as the gas ionises the two swap places.

The ion **number density** rises by a factor of **1.375e5** over the run. An earlier draft of this
report said seven orders of magnitude; that was wrong, because it read the rise in Ar⁺ *mole count*
as a rise in density while the mixture's volume grows **117.6×** over the same interval (3.7188 m³
→ 437.41 m³). Density is what the rate depends on, so 1.375e5 is the figure that belongs here.

### 6.2 What actually happens

**These columns are moles, not mole fractions.** The snapshot writer emits moles; the three columns
sum to 1.0 at t = 0 and to 1.9988 at the end, which is the tell — ionisation creates a second
particle. An earlier draft of this report labelled them mole fractions. Corrected below, with both
normalisations given, because they answer different questions.

Moles, from the solver profiles:

| t (s) | Ar *without* | Ar⁺ *without* | Ar *with* | Ar⁺ *with* |
|---|---|---|---|---|
| 1e-7 | 9.999994e-01 | 5.752334e-07 | 9.999994e-01 | 5.752334e-07 |
| 1e-6 | 9.312061e-01 | 6.879386e-02 | 9.312093e-01 | 6.879060e-02 |
| 3e-6 | 6.438598e-01 | 3.561401e-01 | 6.439562e-01 | 3.560438e-01 |
| 1e-5 | 1.727848e-01 | 8.272152e-01 | 1.734226e-01 | 8.265774e-01 |
| 1e-4 | 6.777791e-09 | 9.999999e-01 | 1.212983e-03 | 9.987870e-01 |
| **1e-3** | **-2.97e-24** | **9.999999e-01** | **1.212976e-03** | **9.987870e-01** |

Final state at 1e-3 s, **in moles**:

```
              without           with              delta
e-(1)    9.999999382e-01   9.987869624e-01   -1.2130e-03
Ar(2)   -5.096717093e-26   1.212975870e-03   +1.2130e-03
Arp(3)   9.999999382e-01   9.987869624e-01   -1.2130e-03
```

The same end state as **total-mixture mole fractions**, which is what a reader expecting fractions
will want:

```
with the entry:   Ar 0.000606856    Ar+ 0.499696572    e- 0.499696572
```

And the **heavy-species neutral fraction**, `Ar/(Ar+Ar⁺) = 1.212976e-3` — a defensible quantity and
the one §6.3 uses, but not what the column header said. The distinction does not touch §6.3's
conclusion: that check is on the **ratio** `Ar/Ar⁺`, which is invariant under any normalisation.

The two trajectories are indistinguishable until ~1e-6 s and then separate. Without the entry the
mechanism has **no loss channel at all** and argon ionises until the neutral is gone. With the entry
the model reaches a balance. (The final `-2.97e-24` mol is numerical noise against `atol=1e-16` —
finite, consistent with the driver's tolerance, and nothing is built on it.)

### 6.3 The steady state is set by this entry, and the arithmetic closes

Equating the mechanism's only two channels, `k_iz·n_e·n_Ar = alpha·n_e·n_Ar+`, predicts
`n_Ar/n_Ar+ = alpha/k_iz` with no free parameters:

```
predicted  alpha / k_iz             = 1.214459e-03
measured   Ar / Ar+  at 1e-3 s      = 1.214449e-03
ratio                                 1.0000
```

**What this establishes, stated precisely, because the first draft overclaimed it.** It is an
*integration consistency check*: the solver was handed these two coefficients and reproduces the
ratio the algebra implies from them. Using unrounded coefficients it agrees to numerical precision,
which is what a correct integrator *should* do. So it confirms that the implementation does what
the rate expressions say — no more. It is **not** an independent validation of the rate, and it is
**not** evidence that either coefficient is right.

With that said: the entry is not a correction to this mechanism's balance, it *is* the balance.
Note also that the no-loss arm does not diverge without bound — it approaches an absorbing state
once the neutral is exhausted — so the contrast between the arms is a difference between a
bounded-by-exhaustion end state and a bounded-by-recombination one, which is less dramatic than
"runaway versus steady state" suggests.

### 6.4 The verdict, stated so it cannot be over-read

The channel is decisive **in this mechanism**, and the reason is a gap, not a virtue: radiative
recombination is the only argon loss channel present, so it sets the balance by default. The
channels that actually dominate argon loss at 5 torr are absent — ambipolar diffusion to the wall,
and dissociative recombination of Ar₂⁺, which I-120 measured at ~2.9e5× faster than this one, and
which I-212 established cannot be represented here at all. A real 5 torr argon glow does not sit at
99.9 % ionisation; it runs at ionisation fractions of order 1e-7 to 1e-5.

So this entry does not make the model right. **It makes the model's end state a recombination
balance rather than an exhaustion state.** The `1.2e-3` heavy-species neutral fraction is a
property of this two-reaction mechanism and must not be quoted as a statement about argon.

**What would have to change for it to stop mattering** is the addition of those loss channels —
and this report does not predict what they would do. Dissociative recombination of Ar₂⁺ depends on
dimer formation and dimer abundance; wall loss depends on transport and geometry. Neither the
dimer nor the geometry is in this model, so their effect on this balance is not calculable from
anything measured here and is not asserted. They are named as absent, which is all the evidence
supports. (I-120 measured Ar₂⁺ dissociative recombination at ~2.9e5× the rate of this channel, and
I-212 established it cannot be represented here at all; a rate ratio is not a steady state, so that
number bounds nothing on its own.)

---

## 7. I-120's ruling has been overtaken on all three supports

I-120 found this exact rate, characterised it fully, and deliberately did not enter it. That was
the right call on the evidence then. Every support has since moved, which is why entering it now is
not a reversal of that judgement but a consequence of the campaign having advanced past it.

| I-120's support | Status now | Evidence |
|---|---|---|
| "Its validity range in Te could not be sourced" | **Addressed by changing source.** Still true of the CHIANTI/AP74 fit I-120 examined — A&A still returns 403, *Rev. Bras. Fis.* 4, 491 still unobtainable. Sidestepped by using SVS82, whose exercised grid is readable (§3.3). | measured |
| "It would be inert — no argon cation has thermochemistry" | **False now.** `PlasmaCationThermo` carries `[Arp]`; the deck builds the reactant and runs. | I-127/I-179 |
| "The problem does not occur at the campaign's working point" | **False at this deck's conditions.** Established at Te = 1 eV, below the Te ≈ 1.33 eV runaway threshold I-120 itself identified. This deck runs at **3 eV**, above it. | §6 |

A fourth item on I-120's "what would unblock it" list has also landed: **`TwoTemperaturePlasma` is
now in `_NET_ELECTRON_KINETICS_CLASSES`**, which is what lets a power-law Te form carry a net
electron count. I-120 ranked that above the argon rate in value, and it is what made this entry
representable in exact form rather than as an approximation.

**Consequence for a sibling library, not acted on here.** `PlasmaArgon`'s `longDesc` still argues
at length that argon radiative recombination "is NOT here, and does not belong", citing I-120. That
paragraph is now stale in all three of its supports. It is flagged in the new entry and here, and
should be revised when `PlasmaArgon` is next touched; editing it was outside this ticket's
verifier and was left alone.

---

## 8. What could not be sourced

Reported because the absence is the finding.

- **The metastable branching fraction — and with it, how much this entry overstates ground-state
  argon.** SVS82's `alpha_r` is the **total** radiative recombination coefficient: capture into the
  ground level plus all excited levels. The product entered here is ground-state Ar alone, so every
  excited-state capture is delivered as if it were a ground-state capture. **This makes the entry an
  unquantified upper bound on ground-state production, and it is labelled as one in the entry.**

  > **Correction.** An earlier draft justified the lumping by comparing the nanosecond radiative
  > cascade against the run's 1e-3 s termination time. That argument is withdrawn: whether an
  > excited state can be eliminated is decided by what competes with its decay — collisional
  > quenching, stepwise re-ionisation out of the excited level, and radiation trapping of the
  > resonance lines, which at 5 torr lengthens effective radiative lifetimes by orders of magnitude
  > — not by whether the bare lifetime is shorter than the simulation. The old text read as a
  > quantitative justification and was not one.

  Argon's metastable 4s `3P2`/`3P0` levels make it concrete: population reaching them is held, not
  delivered. Neither source resolves final states, so the branching fraction is not sourced and the
  size of the overstatement is unknown. (`Ar(3P2)` exists in `PlasmaExcitedNeutralThermo` per I-221,
  but nothing reaches or leaves it, so the branching is not representable here in any case.)
- **Li, Qu & Wang, JQSRT 113 (2012) 1920**, doi:10.1016/j.jqsrt.2012.05.005 — "State-selective
  radiative recombination cross sections of argon ions". **The single highest-value unreachable
  source**, because it is what would quantify the item above.

  > **Correction, and this one was a factual error in my own report rather than in the entry.** The
  > first draft dismissed this source on the grounds that it supplies only cross sections and that
  > no modern independent calculation exists. The publisher's abstract contradicts both: it states
  > the work covers **Ar⁺**, and reports n-, (n,l)- and fine-structure-resolved results together
  > with **Maxwellian rate coefficients and analytic fitting parameters**. A reader who checks finds
  > that in one click, which makes a false dismissal worse than no dismissal.

  The honest position: **the paper could not be retrieved** (ScienceDirect returns HTTP 403), so
  none of its numbers have been seen and nothing here rests on it — it is named as the obvious next
  source, not used as evidence, and not dismissed. If obtained, two things would need checking:
  whether its rate coefficients are usable directly, and its reported finding that Ar⁺ sits near a
  Cooper minimum where simple analytic fits break down — which, if it holds, bears directly on the
  confidence owed to both fits entered and compared here. Note RMG could also take a σ(E) table
  directly via `ElectronCollisionPlasma`, as the `PlasmaArgon` ionisation entry does, so the
  cross-section form would not by itself have been a barrier.
- **Dere et al. 2009, A&A 498, 915 §3** — aanda.org returns 403 on both HTML and PDF, as it did for
  I-120. This is what would give the CHIANTI fit its fitted temperature grid.
- **Aldrovandi & Péquignot 1974, *Rev. Bras. Fis.* 4, 491** — the primary for argon in both chains.
  I-120 established it is not in ADS full text, not on arXiv and not on SciELO; not re-attempted.
- **A modern calculation usable as an entered rate.** None was obtained. The *systematic*
  radiative-recombination programmes (Badnell/APAP, Verner & Ferland, Nahar & Pradhan) are
  organised by isoelectronic sequence and have not reached Cl-like ions, so they do not cover Ar⁺;
  that much is established. But "no modern calculation exists" is **not** established, and this
  report should not have said it — Li, Qu & Wang (above) is exactly such a calculation, it is
  simply unreachable. The accurate statement is narrower and still serious: **both fits that could
  be obtained descend from one 1974 calculation**, which is the deepest limitation on this number,
  and the one source that would break that dependence sits behind a paywall. That is a retrieval
  problem, not a literature gap, and it is more tractable than the first draft implied.

---

## 9. Scope

Nothing under `rmgpy/` was modified — verified with `git status` in the engine worktree. No family
file was touched. No other recombination channel was added. No excited species were added. No
push, merge or PR.

**Changed:**

```
input/kinetics/libraries/PlasmaRadiativeRecombination/reactions.py    + entry index 1, [Arp] => [Ar]
input/kinetics/libraries/PlasmaRadiativeRecombination/dictionary.txt  + [Arp], [Ar]
test/test_plasma_radiative_recombination.py                          fixtures by identity; +22 argon tests
docs/argon-radiative-recombination/                                   this report, decks, logs, profiles
```

No test was deleted or skipped. The only base test id absent afterwards is the deliberate rename
`test_library_loads_with_exactly_one_entry` → `test_library_loads_with_the_expected_coverage`;
verified by diffing `--collect-only` ids against `20cfc36cc`.

The `dictionary.txt` addition was not anticipated and is worth naming: a kinetics library refuses to
load if a species named in an entry label is missing from its dictionary
(`DatabaseError: Species [Arp] ... is missing from its dictionary`). Both new species are written as
adjacency lists taken from the forms already canonical in this database — `[Arp]` from
`PlasmaCationThermo`, `[Ar]` from `primaryThermoLibrary`.

**Referred out:** the family-root defect, both halves, to **I-236**.
