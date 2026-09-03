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
| `Plasma_Electron_Impact_Ionization` | `A_rad → A+` | **+1** | `PlasmaArgon` `Ar+e-⇒Ar⁺+2e-` (Golyatina2021 ECP) | **1.254444e3** m³/(mol·s) |
| `Plasma_Radiative_Recombination` | `A → A⁻` | **−1** | `PlasmaRadiativeRecombination` `Li⁺⇒Li` (Badnell2006 Z=3,N=2) | **1.301428e5** m³/(mol·s) |

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

- **EII ← `PlasmaArgon/reactions.py` entry 86**, `Ar + e- ⇒ Arp + e- + e-`, an
  `ElectronCollisionPlasma` σ(E) table (51-point grid, threshold 15.759 eV). Cited source
  **[Golyatina2021]** (Atoms 2021, 9(90), DOI 10.3390/atoms9040090). This is the campaign's central
  argon reaction; its longDesc documents that it is a cross-section table integrated against a
  Maxwellian EEDF at Te, carried verbatim from `PlasmaAir` index 86.
- **RR ← `PlasmaRadiativeRecombination/reactions.py` entry 0**, `Li⁺ + e- ⇒ Li + hv`, a
  `BadnellRRArrhenius(Z=3,N=2)` fit loaded from `input/kinetics/badnell.yaml`. Cited source
  **[Badnell2006]** (the (Z,N)-indexed radiative-recombination fits; Z=3,N=2 = Li II→Li I;
  A=8.7e-12 cm³/(molecule·s), B=0.364, T0=147 K, T1=7.153e6 K, C=0.1508, T2=7.154e5 K).

Measured at the campaign's 1 eV working point (`get_rate_coefficient(11604.5)`, pinned runtime):

```
EII  PlasmaArgon Ar+e-=>Ar+ +2e- (Golyatina2021 ECP)   : k(1eV) = 1.254444e+03 m^3/(mol*s)
RR   PlasmaRadiativeRecombination Li+=>Li (Badnell Z3N2) : k(1eV) = 1.301428e+05 m^3/(mol*s)
ref  Li EII Voronov Z=3,N=3 (the real Li datum)          : k(1eV) = 1.292979e+08 m^3/(mol*s)
```

The RR value reproduces the `1.301e5` the library's own longDesc quotes at 1.0 eV — independent
confirmation the derivation is faithful.

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
EII  get_kinetics_for_template(['A_rad']) -> A = 1.254444e+03 m^3/(mol*s)   MATCH=True
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

## Precedence (verifier 6), against the post-companion-ticket state

The estimate must not be able to displace a sourced library value. Evaluated as if the family
declarations above already existed:

- **Argon** (EII's own number source): the EII family **cannot produce argon ionisation at all** —
  `generate_reactions([Ar u0 p4 c0]) -> 0 reactions` (probe), because closed-shell argon has u0 and
  the template demands u[1,2,3,4]. So the estimate can *never* overwrite `PlasmaArgon`'s sourced
  argon datum; there is no overlap to lose.
- **Lithium** (the one species with sourced data that the family *does* match): the EII family
  generates `Li⇒Li+`, and the library `PlasmaElectronImpactIonization` also carries it (sourced
  Voronov, 1.29e8). RMG's **library-over-family precedence** decides this at model construction:
  `RMGModel.check_for_existing_reaction` (`rmgpy/rmg/model.py:514-524`) matches a family-generated
  reaction against every loaded `KineticsLibrary` reaction (`are_identical_species_references`) and,
  on a hit, `make_new_reaction` discards the family duplicate. A model that loads the library gets
  the sourced 1.29e8; the family estimate (1.25e3) is suppressed. The same holds for RR at Li⁺.

**Verdict: the estimate cannot displace either sourced value** — it is unreachable for argon and
superseded for lithium. This ticket does not degrade the branch. (An end-to-end deck demonstration
is impossible without the companion code change, and is moot: without the declaration the family
cannot resolve placement at all; with it, the suppression path above applies.)

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
  - worktree (`this input/`): **`1 passed in 409.29s`**

  Both green. Notably the suite stays green *because* neither family has a spectator (Q3) — the
  opposite of the pathfinder's `Plasma_Collisional_Ionization`, which turned it red on
  `kinetics_check_groups_nonidentical`. These two are the clean carry.
- **V5 — 5 torr argon deck unaffected.** Deck `docs/i194-ar5torr-plasma-lineage/input.py` only,
  `rmg.py`, clean run dir, `PYTHON_EXIT` from the interpreter:
  - baseline: `PYTHON_EXIT=0`, one `MODEL GENERATION COMPLETED`, final core **3 species / 1 reaction**
  - worktree: `PYTHON_EXIT=0`, one `MODEL GENERATION COMPLETED`, final core **3 species / 1 reaction**;
    my two families appear **0 times** in stdout/stderr (deck names only `Plasma_Electron_Attachment`
    as a family). baseline == worktree.
- **V6 — libraries still win.** See Precedence above.

---

## Non-goals honoured

No merge/rebase/cherry-pick of `99`; files carried by hand. Neither family added to any set in
`recommended.py` (untouched — `git status` clean for it). No other family touched; no code-repo
edit (`electron_placement.py` untouched — the declaration spec is stated for the companion ticket).
No library value altered. Exactly one estimated entry per family.
