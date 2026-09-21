# I-234 — Argon radiative recombination: sourced, entered, and significant in one observable of two

**The most important finding is not about argon.** Adding this entry silently disabled twenty
existing checks on the lithium entry that was already there — not by breaking an assertion, but by
expiring a fixture precondition, which pytest reports as a setup *error* rather than a failure, so
the checks stopped running while the suite still printed green for the rest. That is §0, and it is
a cleaner instance of this campaign's own subject than anything else here. Fixed; 47 → 69 passing,
zero errors.

**On argon, the result inverts the brief — for one observable, and not for the one the campaign is
chasing.** The brief anticipated that a correctly sourced rate would turn out to be negligible at
5 torr / 3 eV, and asked for the comparison that would establish it. The answer is not one word:

| observable | effect of this entry | verdict |
|---|---|---|
| heavy-species neutral fraction `Ar/(Ar+Ar⁺)` | `0 → 1.213e-3` | **significant** — the only thing producing neutral argon at all |
| electron **density** | `−10.3 ppm` | **negligible** |

Both are the same two committed runs. **This entry is the only loss channel in the mechanism, so it
alone sets the heavy-species balance** — without it argon ionises until the neutral is gone, with it
the model settles at `alpha/k_iz`. But it moves the electron density by ten parts per million,
because at constant pressure the electron gas sets the volume and the mixture shrinks nearly as
fast as the electrons are removed (§6.5). So it is **not** a candidate explanation for the
campaign's electron-density discrepancy, and neither is any other volumetric sink. The channel is
determinative for heavy species for a reason that is itself a finding and not a flattering one
(§6.4).

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

**The fix, and the rule it encodes.** Selection is by identity, not position. The form below is
the *first* version of that fix and is **no longer what ships** — round 66 showed that keying on
the reactant alone collides with a same-reactant second channel, and round 67 showed that even the
right key still has to degrade rather than raise. What ships now is in
`test/plasma_library_selection.py`; the history is kept here because the two wrong versions are
the finding, not an embarrassment to tidy away. Superseded:

```python
def _reaction_for(library, reactant_label): ...   # SUPERSEDED: reactant-only key
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

### 0.1 The same trap was armed in two sibling files — measured, then disarmed

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

**Both are now fixed, and the reasoning that first deferred them was wrong.** My original position
was that the corrected fixture would be a no-op while each library has one entry, with no failing
test to demonstrate it works, so it should wait for whichever commit adds a second entry. Two things
overturned that. First, the objection argues against *inventing* a test to justify the change, not
for leaving a known-armed trap in two files this campaign is actively growing — the fix is the
removal of a hazard, and a hazard does not need a green test to be worth removing. Second, and
decisively: the `i235-three-body-recombination` worktree independently converted this same fixture
in `test_plasma_radiative_recombination.py` to identity selection in its own uncommitted work,
keying on `r.reactants[0].label == '[Lip]'`. That is a second session paying for the same repair
without knowing the first had made it, which is the cost of deferral made concrete.

What changed, in both files:

- the `reaction` fixture selects by the channel it is about — reactants **and** products — and
  hands back an `AmbiguousSelection` rather than raising when that is not unique, so growth can
  never silently disable the checks about the entry that is still there. (As first written this
  bullet said "selects by the reactants it is about" and claimed growth "can never" disable the
  checks. Both were wrong, in rounds 66 and 67 respectively, and the corrected form is above.)
- the count assertion stays in `test_library_loads_with_exactly_one_entry`, where it is a claim
  that fails rather than a precondition that errors. It stays in both files *because* it is
  deliberate in both — each module's own opening docstring argues the smallness is the deliverable
  — which is the one respect this differs from `test_plasma_radiative_recombination.py`, where the
  count was incidental and the test was renamed to pin coverage instead;
- each of those tests additionally pins the coverage *set*, since a bare count is satisfied by any
  second entry, including a wrong one that replaced the entry the file is about.

The collected test-id set was unchanged at 245 **at that commit** — the new assertions were folded
into existing tests rather than added as new ones, so nothing there was a green count bought by
adding tests. It has since moved deliberately and in named steps: **245 → 248** (rounds 66/67 added
one `test_every_reaction_is_distinguishable_from_every_other` per file) **→ 249** (the isolation
receipt, §0.3), with one test renamed. The current number is what the committed
`logs/pytest-round67.stdout.log` shows; where this report quotes 245 it is quoting a past state and
says so.

**The deferral's premise was also simply false, and I only found that out by trying.** I had said
the fix was unverifiable while each library holds one entry. The entry count is a property of the
*loaded* object, and a loaded object can be grown in memory — so it is verifiable. That is worth
naming as a general shape, since it is the same error as §6's: **"I cannot test this" is itself a
claim, and it deserves the same thirty seconds of refutation as any other.** I let it stand
unprobed for a whole session.

The probe written to settle it then became the more instructive failure, twice over, and §0.2
records that instead of the output it originally printed — which described a probe that no longer
exists and a selector that was twice superseded.

### 0.2 The probe was wrong in the same way, twice, and that is the transferable finding

Three versions, each of which could not fail in the direction of the defect it was cited against:

| version | what it injected | what it could not catch |
|---|---|---|
| 1 (round 59) | twin with **reactants renamed** | a same-**reactant** second channel — the actual next growth |
| 2 (round 66) | twin with **products renamed** | a same-reactants-**same-products** duplicate |
| 3 (round 67) | both shapes, plus exit-code and non-empty-baseline guards | — |

Version 2 also reproduced version 1's bug on one library before anyone read its output: in
`Ar + e- => Arp + e- + e-` a single `e-` `Species` sits on **both** sides, `deepcopy` preserves
that sharing, so renaming the products renamed the reactant to `e-**` and the twin could not
collide. It was caught only because version 2 refused to return a twin whose reactants differed
from the original's — a guard on its own premise, which is the thing worth copying.

Version 3 runs `pytest` over the real test files rather than reimplementing the selector, and asks
**errors versus failures** rather than pass counts, because that is the distinction the whole
section is about. Current output, `logs/probe-growth-after.stdout.log`:

```
AS SHIPPED                         passed=102 failed=0 errors=0
GROWN: same reactants, new products passed=100 failed=2 errors=0
GROWN: exact duplicate channel      passed=32  failed=70 errors=0
```

Zero errors in both growth shapes is the whole claim. The negative control for the second row: with
the selector restored to *raising* rather than degrading, the same duplicate injection gives
**5 failed, 32 passed, 65 errors** — so the 70-versus-65 difference is the fix working, not the
probe being lenient.

**Why this shape keeps recurring in probes and not in tests.** Asked directly after the third
instance, because three times in one ticket is a pattern and not bad luck. Four structural reasons,
and they compound:

1. **A test is born red; a probe is born green.** Test-first discipline runs the test before the fix
   exists, so its failure path is exercised by construction. A probe is written *after* the fix, to
   demonstrate it — at the moment of authoring it passes, and its failure path has never once run.
2. **The probe inherits the blind spot of the fix.** Same author, same hour, same model of which
   shapes exist. If that model omits a case, the fix omits it *and so does the probe built to check
   the fix* — and the resulting agreement looks like corroboration.
3. **A probe synthesises its own adversarial input.** A test consumes real data; a probe constructs
   the case. That construction is exactly where the assumption gets baked in — here, which
   participant to rename — and nothing checks the constructor.
4. **A probe is consumed once, by a human, as prose.** It never enters CI and is never observed in a
   state where it should fail, yet its single PASS gets quoted into a report, a commit message and a
   memory. One unexercised path, three supports.

The discipline that follows is cheap: **a probe is not finished until its negative control has been
run**, not merely described — restore the bug, watch it go red, record both numbers. Every claim in
§0.2 above now has one.

### 0.3 What round 67 changed, and the claim it retired

Round 67's finding was that §0.1's guarantee was overstated rather than wrong. `assert_reactions_
uniquely_keyed` adds *one* named failure; it does not stop `reaction_for` raising in every other
fixture, so a genuine duplicate would have produced that named failure **plus** the whole crop of
setup errors the work was meant to eliminate. Two changes make the claim true instead of narrowing
it:

- **`reaction_for` no longer raises.** It returns an `AmbiguousSelection` that raises on first use
  *inside the test body*, so an ambiguous selection is a failure of the test that needed it. The
  measurement above is the receipt.
- **the fixtures are genuinely isolated.** They had always claimed "a fresh reaction per test, so
  mutation cannot leak between them", and that was false: `get_library_reactions` rebuilds the
  participant lists but shares the `Species`, and the reactor tests assign `species.thermo`, which
  landed on the module-scoped library for every later test to read. Nothing depended on it, which
  is what made it worth removing rather than worth ignoring. `test_the_fixture_really_is_isolated_
  from_the_shared_library` is the receipt, and it fails if the deep copy is removed.

---

## 1. The three entry counts, re-run as my own numbers

Re-counted before trusting the brief. All three agree with it.

```
input/kinetics/libraries/PlasmaRadiativeRecombination/reactions.py    -> 1 entry:  [Lip] => [Li]
                                          (as of the START of this ticket; it ships TWO now,
                                           [Lip] => [Li] and the [Arp] => [Ar] added below)
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

## 6. Does it matter? In one observable yes, in the other no

> **Reproducibility, stated before the numbers rather than after them:** the two arms below are
> **not** reproducible from the committed files as they stand. `run-with/input.py` and
> `run-without/input.py` are byte-identical, because the two arms differ by the *database*, not by
> the deck: the without-arm was produced by temporarily reverting tracked library files to their
> pre-entry state. Re-running both decks at this commit reproduces the with-entry arm twice. The
> exact procedure to reproduce the without-arm is in §5.1. The committed evidence for the
> without-arm is its `solver/simulation_1_3.csv` and its captured streams, not its deck.


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

### 6.5 The observable the branch never stated: electron density moves by 10 ppm

Round 66 caught this and it is a labelling error of mine, not a measurement error. Everything in
§6.2–§6.4 is about the *heavy-species* composition, where this channel is decisive. The campaign's
actual target is the **electron density**, and until now no number for it appeared anywhere on this
branch. Recomputed here from the same two committed profiles (end state, `(with − without)/without`):

| quantity | with | without | Δ |
|---|---|---|---|
| electron amount (mol) | `0.9987869624` | `0.9999999382` | `−1213 ppm` |
| mixture volume (m³) | `437.411536` | `437.9382338` | `−1203 ppm` |
| **electron density (mol/m³)** | `2.2834033e-03` | `2.2834269e-03` | **`−10.3 ppm`** |
| heavy neutral fraction `Ar/(Ar+Ar⁺)` | `1.213e-3` | `−2.5e-26` | `0 → 1.2e-3` |

**Why the amount moves 118× more than the density.** At constant pressure the two-temperature
equation of state is

    V = R·((n_total − n_e)·T_gas + n_e·T_e) / P

With this deck ionised essentially to completion and `T_e/T_gas = 116.8`, the electron gas carries
**99.15 %** of that bracket. Removing 1213 ppm of the electrons therefore removes 1203 ppm of the
volume along with them, and the density — their quotient — moves only by the residue, 10.3 ppm.
The volume cancels out of any *ratio* of two heavy species, which is precisely why the neutral
fraction is free to move three orders while the density is pinned.

**Two things I previously offered as checks, corrected — neither is independent evidence.**

- `1 − 99.15 % = 0.85 %`, and `1213 × 0.0085 = 10.3`, against a measured `10.31`. I presented this
  as the EOS being confirmed rather than asserted. **It is not.** The `0.85 %` is computed from the
  same final composition, through the same equation of state, that produced the volume the
  measurement divides by — so the multiplication is a first-order restatement of an identity, and
  it would come out right whether or not the EOS were the *cause* of anything. It is an **internal
  consistency check**: it says the numbers in the table are mutually coherent and that I have not
  dropped a factor. That is worth having and worth keeping. It is not a second derivation, and the
  campaign ledger's "two derivations, two data sets, one number" was withdrawn on the same grounds.
  What actually supports the causal claim is that the mechanism is standard and that the same
  suppression appears on an unrelated channel (I-235's three-body, `−4.35 ppm` at the same ~1/117).
- the two arms stop at different simulation times (`1.394e-3` vs `1.303e-3` s), so I interpolated
  both to the earlier arm's final time and got the same `−10.3 ppm`. **That check is vacuous**, and
  saying so is more useful than the check: the with-arm rows bracketing that time are bit-identical,
  so the interpolation returns the same numbers it was given. It answers the termination-time
  objection — the end state is not still moving — and it adds no validation beyond that. It is
  reported here as an objection disposed of, not as a second measurement.

**What this means for the campaign, with its boundary stated.** No volumetric electron sink, of
any order, can close an electron-density discrepancy in this deck: every one of them removes
electrons and shrinks the volume in near-lockstep, and only the ~1/117 residue survives into the
density. That covers radiative recombination here, I-235's three-body channel, and any future
dissociative-recombination entry.

**The boundary, which the earlier phrasing left out.** The suppression factor is
`1 − f`, where `f` is the electron gas's share of the EOS bracket `(n_heavy·T_gas + n_e·T_e)`, and
`1 − f → T_gas/T_e` only in the **fully ionised** limit at fixed `P`, `T_gas` and `T_e`. A sink
strong enough to de-ionise the mixture walks out of that limit as it acts: as `n_e` falls, `f`
falls, and the suppression weakens toward nothing — a weakly ionised deck, where the heavy gas sets
the volume, has no suppression at all. So the correct statement is **not** "no volumetric sink can
ever matter", it is "no volumetric sink can matter *while the electron gas still dominates the
bracket*", which is a self-limiting condition rather than a permanent one. The wall-operator work
reached the same boundary independently, which is mild corroboration that it is the right place to
draw it. The channels that could move the density *without* that caveat are the **non-volumetric**
ones — ambipolar diffusion and wall loss, which act as a surface operator and are absent from this
mechanism entirely.

This does **not** weaken the entry. The rate is unchanged, the source is unchanged, and the
heavy-species finding in §6.2–§6.4 stands exactly as measured. What changes is the label on it:
significant for heavy-species composition, negligible for electron density.

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

**Which runaway threshold, and why there are two numbers.** The 1.33 eV above is I-120's figure and
is quoted as I-120 stated it. I-237 has since measured the same crossover at **1.4247 eV**, and the
difference is not an error in either: I-120 compared radiative recombination against the **Voronov**
fit in `voronov.yaml`, while I-237 compared it against the **Golyatina2021 cross-section table
`PlasmaArgon` actually ships** and this deck actually integrates. The shipped-table figure is the
one that applies to the deck as built. Nothing in this section turns on which is used — this deck
sits at 3 eV, above both — but anyone carrying the threshold forward should carry 1.4247 eV and cite
I-237, not carry 1.33 eV out of this table. I-237's calculation also corroborates §6 of this report
from outside it: its `alpha/k_iz = 1.2144e-03` reproduces the neutral fraction measured here from
the solver, `1.214449e-03`, to four significant figures without running a reactor.

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

  > **Retrieval re-attempted 2026-09-15, re-queried and scoped 2026-09-21.** The question was
  > whether 403 from ScienceDirect meant "no copy exists" or merely "not by that route". OpenAlex
  > returns for this DOI, as work `W2079986418`:
  >
  > ```
  > open_access.is_oa                          false
  > open_access.oa_status                      "closed"
  > open_access.oa_url                         null
  > open_access.any_repository_has_fulltext    false
  > best_oa_location                           null
  > locations_count                            1
  > locations[0]                               is_oa false, pdf_url null,
  >                                            landing_page_url = the publisher DOI
  > ```
  >
  > **Status: UNESTABLISHED. Read the block above as an observation, not a finding.** This has now
  > been narrowed twice and the honest move is to stop narrowing and label it. What the record
  > supports is exactly one sentence: *a query to OpenAlex for this DOI reported no open-access
  > location*. Everything I built on that has been more than it carries —
  >
  > - "no open copy indexed anywhere" → OpenAlex is not exhaustive, and it is one index;
  > - "a paywall rather than a search failure" → **still too strong.** A negative index record
  >   does not distinguish a paywalled work from one whose open copy is simply unharvested. I do
  >   not know which this is;
  > - the field values themselves → transcribed through `WebFetch`'s summarising model, because
  >   direct `curl` to `api.openalex.org` is blocked by this environment's sandbox. **No raw
  >   response was preserved, in either attempt.** An unverified reading of an index is thin
  >   evidence even for the one sentence above.
  >
  > What this means practically is unchanged and does not depend on the above: **nothing in this
  > report uses any number from this paper**, and obtaining it needs a route this session does not
  > have. The next session should treat the retrieval as *open and unattempted by any means that
  > would settle it*, not as closed — and should capture a raw response if it re-queries.
  >


  The honest position: **the paper could not be retrieved here** (ScienceDirect returns HTTP 403), so
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
