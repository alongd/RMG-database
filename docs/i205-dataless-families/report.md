# I-205 — carrying the two data-less plasma families, each with a sourced estimated rule

**Worktree:** `/home/alon/Code/RMG-database-i205-dataless`, branch `i205-dataless` (cut from
`plasma`, 0 behind). **Code repo (read-only):** `/home/alon/Code/RMG-Py-plasma`@`plasma` tip
`4910d8c52`, built (46 `.so`). **Baseline DB:** `/home/alon/Code/RMG-database-plasma/input`.
All runtime results used `conda activate rmg_env` and `PYTHONPATH=/home/alon/Code/RMG-Py-plasma`.

Two families carried from branch `99`, translated per
`docs/plasma_family_carry_translation_rule.md`, each given ONE estimated rate rule derived from
this branch's own sourced library:

| Family | template | `electrons` | estimated rule source | k(1 eV) frozen as A |
|---|---|---|---|---|
| `Plasma_Electron_Impact_Ionization` | `A_rad → A+` | **+1** | `PlasmaElectronImpactIonization` `Li⇒Li⁺` (Voronov1997 Z=3,N=3) | **1.292979e8** m³/(mol·s) |
| `Plasma_Radiative_Recombination` | `A → A⁻` | **−1** | `PlasmaRadiativeRecombination` `Li⁺⇒Li` (Badnell2006 Z=3,N=2) | **1.301428e5** m³/(mol·s) |

> **Anchor change (2026-09-04, owner ruling).** The EII estimate was ORIGINALLY anchored on argon
> ionisation (`PlasmaArgon`, Golyatina2021 ECP, **k(1 eV) = 1.254444e3 m³/(mol·s)**) — that number is
> kept here on the record, not silently dropped. It was **re-anchored onto the sourced Voronov
> lithium datum** because an order-of-magnitude placeholder should rest on chemistry the family can
> actually be asked about: this family *cannot generate argon at all* (`generate_reactions([Ar])→0`,
> u0 ∉ template u[1,2,3,4]), whereas it does generate `Li⇒Li⁺`. Lithium is equally sourced and
> citable, so provenance is unchanged and the range-of-validity statement is now defensible (§V6,
> §"range of validity"). RR's anchor is unchanged. The rewritten sections below are EII's; RR's
> stand as first written.

---

## The four probe questions

### Q1 — the translation rule, and the `electrons` value it implies for each family

The rule (5 edits: strip `e-` from `template`, delete `custom_kinetics`, rename
`product_electrons`→signed `electrons`, drop the `e-` group node + tree line, relabel charged
species — none here since both training sets are empty). `electrons` is the signed net = electrons
the forward reaction **produces − consumes**, cross-checked against `family.py:1574-1583` charge
balance.

- **`Plasma_Electron_Impact_Ionization`** — forward `A + e- ⇒ A⁺ + e- + e-`: produces 2, consumes
  1 → **`electrons = +1`**. (`99` carried `product_electrons = 2`; the *net* is +1 because one
  electron is consumed on the reactant side — not a verbatim value copy.) Charge check: template
  after strip `A_rad → A⁺`, reactant net 0, product net +1; `family.py:1581` does
  `product_net_charge -= electrons` → `+1 − 1 = 0`. Balances.
- **`Plasma_Radiative_Recombination`** — forward `A + e- ⇒ A⁻`: produces 0, consumes 1 →
  **`electrons = −1`**. (`99` carried `product_electrons = 0`, which is **wrong** — it would leave
  products at −1 and the reaction silently dropped. The rename must compute the signed net, and
  this family is exactly the case the translation rule's "rename, don't copy" clause exists for.)
  Charge check: `A → A⁻`, product net −1; `−1 − (−1) = 0`. Balances. Matches `Plasma_Electron_Attachment`.

### Q2 — the library entries derived from, and their provenance

Both provenances are deep and citable (not thin — the derivation is legitimate):

- **EII ← `PlasmaElectronImpactIonization/reactions.py`** entry `[Li] => [Lip]`
  (`Li(2S) + e- ⇒ Li⁺ + 2e-`), a `VoronovEIArrhenius(Z=3,N=3)` fit loaded by (Z,N) from
  `input/kinetics/voronov.yaml`. Cited source **[Voronov1997]** (G.S. Voronov, "A Practical Fit
  Formula for Ionization Rate Coefficients of Atoms and Ions by Electron Impact: Z = 1–28", Atomic
  Data and Nuclear Data Tables 65 (1997) 1–35; Table I, Z=3 N=3 = Li I→Li II, threshold dE = 5.4 eV;
  valid Te = 1 eV–20 keV). *(Original anchor, kept on record: `PlasmaArgon` entry 86
  `Ar+e-⇒Ar⁺+2e-`, `ElectronCollisionPlasma` σ(E) table, 51-pt grid, threshold 15.759 eV,
  **[Golyatina2021]** Atoms 2021 9(90) DOI 10.3390/atoms9040090, k(1 eV)=1.254444e3.)*
- **RR ← `PlasmaRadiativeRecombination/reactions.py` entry 0**, `Li⁺ + e- ⇒ Li + hv`, a
  `BadnellRRArrhenius(Z=3,N=2)` fit loaded from `input/kinetics/badnell.yaml`. Cited source
  **[Badnell2006]** (the (Z,N)-indexed radiative-recombination fits; Z=3,N=2 = Li II→Li I;
  A=8.7e-12 cm³/(molecule·s), B=0.364, T0=147 K, T1=7.153e6 K, C=0.1508, T2=7.154e5 K).

Measured at the campaign's 1 eV working point (`get_rate_coefficient(11604.5)`, pinned runtime):

```
EII  PlasmaElectronImpactIonization Li=>Li+ (Voronov Z3N3)  : k(1eV) = 1.292979e+08 m^3/(mol*s)  [anchor]
RR   PlasmaRadiativeRecombination  Li+=>Li  (Badnell Z3N2)   : k(1eV) = 1.301428e+05 m^3/(mol*s)  [anchor]
--   PlasmaArgon Ar+e-=>Ar+ +2e-   (Golyatina2021 ECP)       : k(1eV) = 1.254444e+03 m^3/(mol*s)  [EII original anchor, superseded]
```

The RR value reproduces the `1.301e5` the library's own longDesc quotes at 1.0 eV — independent
confirmation the derivation is faithful. The two EII endpoints (Li 1.29e8 vs Ar 1.25e3) sit five
orders apart: that spread is threshold physics (Li 5.4 eV vs Ar 15.76 eV at Te = 1 eV) and is
exactly why the anchor choice governs the range-of-validity statement, not the provenance.

### Q3 — the two structural walls

- **(a) atom-type perception** — N/A for both. Both training sets are **empty** on `99` (nothing to
  perceive), and the template groups are generic (`R u[1,2,3,4]…` / `R u0…`), not concrete species.
- **(b) spectator tripping `kinetics_check_groups_nonidentical`** — N/A for both. Neither family has
  a molecular spectator: the only species on both sides was the electron `e-`, which edit 1 strips
  into the `electrons` scalar. (Contrast `Plasma_Collisional_Ionization`, whose `M` spectator is the
  reason it was held out — recorded in the translation rule doc §"the spectator". These two are the
  clean case.) Confirmed downstream by the standing DB test (Q4/verifier 4).

### Q4 — the exposure this ticket closes

**Before** (family with no rule): a family asked to estimate returns **nothing usable** and, on a
plasma reactor, hard-fails. The precise failure is `ElectronPlacementError` — see the electron-
placement finding below.

**After**: the family returns the estimated value on request. Rate-rule retrieval against the
built family (probe `probe_families.py`):

```
EII  get_kinetics_for_template(['A_rad']) -> A = 1.292979e+08 m^3/(mol*s)   MATCH=True   (Voronov Li anchor)
RR   get_kinetics_for_template(['A'])     -> A = 1.301428e+05 m^3/(mol*s)   MATCH=True
```

Each equals, to the last quoted digit, the sourced library value it came from (Q2) — because it
*is* that value, evaluated once at 1 eV and frozen. No fitting, no invention.

---

## Form chosen: a rate RULE, not a training reaction (one paragraph, as required)

I put the estimate as a hand-written `Arrhenius` **rate rule on the root node** (`rules.py`), not
as a training reaction. Three reasons. (1) The deliverable is literally "one sourced reaction's
kinetics promoted to a **top-node rule** for a whole family" — a root rule is that; a training
reaction is a per-species datum that happens to average up. (2) A training reaction needs a
concrete species carrying the number, and there is no honest one: EII's number is argon's, but
argon **cannot be a training species in this family** (closed-shell, u0 ∉ template u[1,2,3,4]), and
any substitute radical would mislabel argon's datum as that species' own; RR's number is Li⁺'s, and
a Li⁺ training reaction would **duplicate — and be confusable with — the sourced library entry**
this ticket must keep the estimate distinct from. (3) A plain `Arrhenius` is the only representable
type regardless: `add_rules_from_training` and `average_kinetics` accept only `Arrhenius`/Surface*
(stated in `Plasma_Electron_Attachment/training/reactions.py`), so `ElectronCollisionPlasma`/
`VoronovEIArrhenius`/`BadnellRRArrhenius` could not be carried as-is anyway. The estimate is
`Arrhenius(A=k(1 eV), n=0, Ea=0)`, `rank=10` (poor; smaller=better, auto-fits use 11), with a
`shortDesc` beginning `ESTIMATE —` and a longDesc stating provenance, that it is a one-point
generalization, and where it is/ isn't defensible.

---

## Electron-placement finding (scope addition): the exact declaration each family needs

`rmgpy/electron_placement.py`'s `FAMILY_ELECTRON_PLACEMENT` is keyed on `Reaction.family`, and
`resolve_electron_placement` **hard-fails by name** for any owner absent from it (no net-derived
fallback). The map contains the two *library* labels (`PlasmaRadiativeRecombination:(1,0)`,
`PlasmaElectronImpactIonization:(1,2)`) but **neither family label** (underscored). So each family,
the moment it is asked to produce a reaction, raises `ElectronPlacementError` — confirmed, not
assumed (`probe_families.py`):

```
EII  generate_reactions([Li u1]) -> <[Li]> => <[Li+]>   family='Plasma_Electron_Impact_Ionization'
     resolve_electron_placement -> ElectronPlacementError: Family 'Plasma_Electron_Impact_Ionization'
     has no electron-placement declaration (... electrons=1); ... Only owners declared in
     FAMILY_ELECTRON_PLACEMENT can resolve.
RR   generate_reactions([Li+ u0]) -> <[Li+]> => <[Li]>  family='Plasma_Radiative_Recombination'
     resolve_electron_placement -> ElectronPlacementError: Family 'Plasma_Radiative_Recombination'
     has no electron-placement declaration (... electrons=-1); ...
```

**The declarations the companion CODE ticket must add** (I did NOT edit `electron_placement.py`):

| family label | `(reactant_count, product_count)` | reasoning | matches sibling library? |
|---|---|---|---|
| `Plasma_Electron_Impact_Ionization` | **(1, 2)** | incident order 1 (one e⁻ in); product 2 (two e⁻ out); net = 2−1 = +1 = `electrons` | **Yes** — identical to library `PlasmaElectronImpactIonization` (1,2); same forward electron bookkeeping |
| `Plasma_Radiative_Recombination` | **(1, 0)** | incident order 1 (one e⁻ captured); product 0 (none out); net = 0−1 = −1 = `electrons` | **Yes** — identical to library `PlasmaRadiativeRecombination` (1,0); electron captured, none emitted, whatever the charge stage |

Both match their sibling library's pair exactly, so the companion ticket adds two rows with numbers
already validated here. (`reactant_count` = incident order, which the rate coefficient's
dimensionality must match; `product_count − reactant_count` = the net, independent of it.)

---

## Precedence (verifier 6), against the post-companion-ticket state — now with the lithium anchor

The estimate must not be able to displace a sourced library value. The re-anchor makes this the
sharp case: the EII estimate is now anchored on the very Voronov Li datum the family also matches, so
Li is exactly where an estimate could shadow real data. Executed (`probe_prec.py`,
`probe_prec3.py`), not asserted from code-reading as the first report's version was.

- **Argon** (EII's *original* source): the EII family **cannot produce argon ionisation at all** —
  `generate_reactions([Ar u0 p4 c0]) -> 0 reactions`, because closed-shell argon has u0 and the
  template demands u[1,2,3,4]. So the estimate can never overwrite `PlasmaArgon`'s sourced argon
  datum; there is no overlap to lose. (This is also why argon was a poor anchor — hence the swap.)
- **Lithium** (the species with sourced data the family *does* match, and the new anchor): the EII
  family generates `Li⇒Li+`; the library `PlasmaElectronImpactIonization` carries the sourced Voronov
  `Li⇒Li+` (k(1 eV)=1.292979e8). Suppression is decided by
  `RMGModel.check_for_existing_reaction` (`rmgpy/rmg/model.py`, library loop lines 508–534), and its
  match test `are_identical_species_references` compares **not only the heavy species but the
  electron-placement counts** (`get_electron_placement_counts`, `rmgpy/electron_balance.py`).
  Measured, both states:

  ```
  library placement counts                         : (1, 2)
  CURRENT (family undeclared):
    family placement counts                        : (0, 1)   <- net-scalar fallback, != library
    are_identical_species_references(fam, lib)     : False    -> family NOT suppressed
  POST-COMPANION-TICKET (family declared (1,2)):
    family placement counts                        : (1, 2)   == library
    are_identical_species_references(fam, lib)     : True
    check_for_existing_reaction -> found, returns LibraryReaction  -> family estimate SUPPRESSED
  ```

  So a model gets the **sourced Voronov Te-dependent fit**, not the flat 1 eV estimate. The estimate
  cannot shadow the sourced Li value. (The `CURRENT` row is moot in a real run: without the
  declaration the family raises `ElectronPlacementError` at solve time and never coexists with the
  library at all.)

**Verdict: the estimate cannot displace either sourced value** — unreachable for argon, suppressed
for lithium. **No regression from the swap.** The precedence outcome is value-independent (it turns
on reaction *identity*, not rate magnitude), so it is the same for the old argon anchor and the new
lithium one; the first report's conclusion was directionally right but is now confirmed by execution.

**Load-bearing corollary for the companion ticket.** The suppression HINGES on the family's declared
pair equalling the library's `(1,2)`. The `(1,2)` I specified is therefore load-bearing *twice*: it
lets the family run (resolves `ElectronPlacementError`) AND it is exactly what makes the sourced
library win over the family estimate. A *different* declared pair would let the estimate coexist with
— and shadow — the sourced datum. Declare `(1,2)` for EII and `(1,0)` for RR, not merely "some pair".

### Disposition of the I-206 adversarial-review HIGH (which owner wins, and can the estimate displace the sourced value)

The review is correct that `are_identical_species_references` (`model.py:2356`) compares heavy-species
references and per-side electron-placement counts and **nothing else** — no owner, no kinetics, no
provenance, no rate comparison. Once I-206 declares the family `(1,2)`, a family `Li⇒Li+` and the
library's sourced Voronov `Li⇒Li+` compare identical, and `check_for_existing_reaction` returns the
incumbent while `make_new_reaction` drops the newcomer silently. So the protection is **entirely
registration order**; there is no source-priority rule that would save the sourced value if the order
were reversed. Verified against the code, each point:

1. **Collision scope is lithium-only.** The `PlasmaElectronImpactIonization` library has exactly ONE
   entry, `[Li]⇒[Lip]` (`len(lib.entries)==1`). The family generates ionisation for every radical
   (measured: `N⇒N+`, `O⇒O+`, and `Li⇒Li+`), but the only heavy-species overlap with the library is
   **Li**. For N, O, H, Si… the library has no entry, so the estimate is the sole (intended) source
   and displaces nothing. The collision the review names is real but narrow: it is lithium and only
   lithium.

2. **In a normal run the sourced value wins, by initialization order — not merely "usually".** The
   library reaction enters the model **wholesale at `initialize()`** via `add_reaction_library_to_edge`
   (`main.py:795-796`), which runs strictly before the family-enlargement loop. So the sourced
   Voronov `Li⇒Li+` is always the pre-loaded incumbent; when the family later generates `Li⇒Li+` it is
   always the newcomer that gets dropped. There is no enlargement-time path in which the family
   reaction precedes the library one. (Note: the review's `generate_reactions` library-before-family
   ordering, `database.py:464-465`, does not even come into play here — `generate_reactions_from_libraries([Li])`
   returns `[]`, i.e. the library's Li reaction is not surfaced by on-the-fly generation at all; it is
   present only because it was pre-loaded. That makes the ordering guarantee stronger, not weaker.)

3. **Plain disposition.** Under normal operation — any run loading both the library and the (post-I-206)
   family — **the estimate provably cannot displace the sourced Voronov value**: the library is the
   pre-loaded incumbent and the family duplicate is dropped. The estimate becomes the operative lithium
   rate only under conditions that involve **no sourced value to displace or a deliberately inverted
   load order**, named honestly:
   - (a) a deck that loads the family but **not** the library — then there is no sourced Voronov value
     in the model; the estimate is the intended fallback, displacing nothing;
   - (b) the pathological ordering where a family-generated estimate is baked into a **seed mechanism**
     (added to core at `main.py:790-791`, ahead of reaction-library loading at `795-796`) and a later
     run loads both that seed and the library — then the seed estimate is the incumbent and the library
     reaction is the dropped newcomer. This is a deliberate, self-inflicted configuration, not normal
     operation; I observe the ordering in code (`790` precedes `795`) but did **not** construct the
     seed to confirm it end-to-end, and it is outside this ticket's data.

   The estimate is not resolved by weakening it or removing the family — that is the owner's call, not
   mine; this report states the mechanism and its exact conditions so he can make it. **Bottom line:
   in normal operation the sourced Voronov value is not displaceable by the estimate, but the
   guarantee rests solely on RMG's registration order (libraries pre-loaded before family enlargement),
   because the identity check carries no source-priority of its own.**

---

## Verifier results

- **V2 — each family loads and is what I think it is.** Loaded alone from this worktree's `input/`
  (`probe_families.py`): EII template `['A_rad']→['A+']`, `electrons=1`, one rule on `A_rad`
  rank 10; RR template `['A']→['A-']`, `electrons=-1`, one rule on `A` rank 10. Quoted above.
- **V3 — estimate reachable, returns the intended number.** Rate request in, value out, MATCH=True
  for both (Q4).
- **V4 — standing DB test no worse than baseline.** `test/database/databaseTest.py::TestDatabase::test_kinetics`,
  one suite per process (verifier 7), each with its own rmgrc:
  - baseline (`RMG-database-plasma/input`): **`1 passed in 501.90s`**
  - worktree, original argon anchor (`this input/`): **`1 passed in 409.29s`**
  - worktree, after re-anchor to Voronov Li: **`1 passed in 425.05s`**

  All green. The DB structural test is value-independent (it checks tree/group consistency, not rate
  magnitudes), so the re-anchor cannot change its result — re-run anyway on the owner's instruction.
  Notably the suite stays green *because* neither family has a spectator (Q3) — the opposite of the
  pathfinder's `Plasma_Collisional_Ionization`, which turned it red on
  `kinetics_check_groups_nonidentical`. These two are the clean carry.
- **V5 — 5 torr argon deck unaffected.** Deck `docs/i194-ar5torr-plasma-lineage/input.py` only,
  `rmg.py`, clean run dir, `PYTHON_EXIT` from the interpreter:
  - baseline: `PYTHON_EXIT=0`, one `MODEL GENERATION COMPLETED`, final core **3 species / 1 reaction**
  - worktree, original anchor: `PYTHON_EXIT=0`, one `MODEL GENERATION COMPLETED`, core **3 / 1**;
    my two families appear **0 times** (deck names only `Plasma_Electron_Attachment`).
  - worktree, after re-anchor: `PYTHON_EXIT=0`, one `MODEL GENERATION COMPLETED`, core **3 / 1**,
    families 0 mentions. Unchanged — the deck loads neither family, so the estimate's value is inert to it.
- **V6 — libraries still win.** See Precedence above; confirmed by execution against the
  post-companion-ticket state, and value-independent.

---

## Non-goals honoured

No merge/rebase/cherry-pick of `99`; files carried by hand. Neither family added to any set in
`recommended.py` (untouched — `git status` clean for it). No other family touched; no code-repo
edit (`electron_placement.py` untouched — the declaration spec is stated for the companion ticket).
No library value altered. Exactly one estimated entry per family.
