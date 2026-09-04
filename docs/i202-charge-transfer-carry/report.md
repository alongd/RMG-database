# I-202 — Carry `Plasma_Charge_Transfer` from branch `99`, translated

Worktree `RMG-database-i202-chargetransfer` (branch `i202-chargetransfer`, cut from `plasma`, 0 behind).
Code read-only from `RMG-Py-plasma@plasma`. Rule applied:
`RMG-database-i200-collisional/docs/plasma_family_carry_translation_rule.md`.

## Outcome (headline)

**The family is fully translated but HELD OUT of `input/` (staged under
`docs/i202-charge-transfer-carry/staged-family/`), per decision.** It cannot land green: the
branch-99 group tree fails the target branch's `kinetics_check_sample_descends_to_group` on **four**
group nodes, and repairing them is group-definition work beyond both the translation rule and the
minimal tree fix I was authorised to make. The worktree suite is therefore at baseline (green); the
group-tree repair is a companion task (§6). Not pushed, not merged (both gated). This mirrors the
pathfinder's disposition for its own blocked family (`Plasma_Collisional_Ionization`, held out of
`input/`).

The translated family loads correctly as a unit (24 of 28 training entries; 4 NO+ held) — the block
is only the group-tree sampler, and only surfaces via the standing suite.

---

## 1. What the rule implies for THIS family, edit by edit

Charge exchange — `A+ + B <=> A + B+`, `A+ + B- <=> A + B`, `A++ + B- <=> A+ + B`. An electron moves
between heavy species; **the free-electron pool is never touched.** That single fact reshapes the edits.

| Rule edit | This family | Result |
|---|---|---|
| 1. Strip `e-` from template | **no `e-`** anywhere (template `["A","B"]→["A-","B+"]`) | **no-op** |
| 2. Delete `custom_kinetics` | `custom_kinetics = False` present | deleted |
| 3. `product_electrons=N` → `electrons=±N` | `product_electrons = 0` | `electrons = 0` |
| 4. Label-safe charged species | many `+`/`-` in labels (§4) | `+`→`p`, `-`→`m` |
| 5. Training set travels unchanged | 28 entries | carried, kinetics/desc verbatim |

**`electrons` must be `0`** — charge transfer produces zero net free electrons. Unlike the
pathfinder's `Plasma_Collisional_Ionization` (verbatim-99 loaded `0`, correct value `1`), here
**verbatim and translated agree at `0`**: the loader seeds `electrons=0` by default and ignores
`product_electrons`, so the rename does not change the loaded value. It is still correct-by-convention,
but for this family it is *not* what makes the copy right — the copy fails elsewhere (§4, §6).

### Dangling `reverse` and phantom products — both inert (verified)
- `reverse = "Plasma_Charge_Transfer_Reverse"` names a family that **does not exist even on `99`**.
  `family.py:715` reads it as a *string*; it never loads another family during `load`, so it cannot
  fail. Carried verbatim.
- `products=["A-","B+"]` name undefined entries. `family.py:717` **regenerates** the product template
  from the reactants for a non-own-reverse family, so the declared strings are never looked up.

## 2. The two structural walls the pathfinder hit

**(a) Atomtype perception — HITS here.** Probing all 39 dictionary species through
`Molecule().from_adjacency_list` on the target code, exactly one fails:

```
NO+_r1: AtomTypeError: Unable to determine atom type for atom N+, ... 1 double bonds (1 to O) ...
```

Same charge-on-N nitrosonium the rule flagged. `N2+` (charge on N, *triple* bond) perceives fine;
only double-bonded `NO+` fails. Used by 4 training entries (14, 16, 17, 21) → **held** (§5). This is
also why a verbatim-99 copy fails outright: `get_species` perceives the dictionary on load and
crashes on `NO+_r1` before any reaction is built.

**(b) Spectator — does NOT apply.** By construction: recipe `LOSE_CHARGE *1` / `GAIN_CHARGE *2`
modifies **both** template atoms, so no species is unchanged across the arrow;
`kinetics_check_groups_nonidentical` cannot trip. Suite confirms (no such error).

## 3. The training set

Both `training/*` files travel with the family. No kinetics value, `shortDesc`, or `longDesc` altered.
24 of 28 entries load (loaded set quoted in §7); 4 NO+ entries held as comments preserving kinetics
and references.

## 4. Label translation — why `+` MUST change and `-` need not (but does, per rule)

The training loader splits reactant/product strings on **bare `+`** (`depository.py:207,216`), then
strips whitespace. `H+_r1` → `['H','_r1']`; trailing `+` (`O+`, `N2+`) → empty token. **Every `+` in
a label breaks loading and must become `p`.** `-` does not split (the sibling family
`Plasma_Electron_Attachment` keeps `O2-`, `OH-`, `O-` literally on this same branch).

**Finding — the rule's `-`→`m` is stricter than necessary for this family.** I followed it
(`H-_r2`→`Hm_r2`), but `Plasma_Electron_Attachment` proves `-` in labels loads fine here. Both forms
load; `-`→`m` is rule-compliant and internally consistent. Flagged, not deviated. `_r1`/`_r2`
reactant-slot tags are already label-safe and kept; no rename collisions (`Op_r1`≠`Op`, `Np_r1`≠`Np`,
`O2p_r1`≠`O2p`).

## 5. NO+ — held (decision)

The 4 NO+ entries (14, 16, 17, 21) are held as comments, matching the pathfinder precedent and
avoiding a gated species-identity change. Each comment keeps the entry's kinetics/reference and
records the correct `[N#O+]` (charge on O, triple bond) for one-step re-enable. 24/28 land.

## 6. Group-tree defects — the reason it can't land, and the upstream divergence

### 6a. The authorised fix (H_ion / H2_ion siblings) — applied, changes NO match
`test_kinetics` first went red on `kinetics_check_siblings_for_parents`:

```
In family Plasma_Charge_Transfer, node H_ion is a parent of H2_ion, but they are written as siblings.
```

**Real defect, not a false-positive:** `match_node_to_child(H_ion, H2_ion)=True`, reverse `=False` —
`H_ion` (`*1 H u0 p0 c+1`) is a genuine ancestor of `H2_ion`, yet `99` writes both as siblings under
`H_cation`. Fixed by re-nesting (ordering-only; no adjacency/kinetics/identity edit):

```
    L2: H_cation           |        L2: H_cation
        L3: H_ion          |            L3: H_ion
        L3: H2_ion   --->  |                L4: H2_ion
```

**Upstream divergence — flagged.** This edits `groups.py`, a file shared with branch `99`. **`99`
still carries this defect** on the `H_ion`/`H2_ion` pair — an upstream-reportable bug; our staged
family deliberately diverges from `99` here.

**Does it change any match? NO — enumerated.** `get_reaction_template_labels` on all 24 loadable
training reactions, before (siblings) vs after (nested): **TOTAL CHANGED = 0** (every entry maps to
the same template node). Mechanism: the training species `H2p_r1` is carried from `99` as a
**disconnected** structure (`H` radical + bare `H+`, no bond), while the `H2_ion` group requires a
`{2,S}` bond — so `match_node_to_structure(H2_ion, H2p_r1)=False` in both trees. The only H2+ datum
can never reach `H2_ion`; it matches `H_ion` and descends there before and after. `H2_ion` is
unreachable by present training data, so re-nesting is inert for every existing match. Only a
*hypothetical future* bonded-H2+ reactant's estimation fallback parent moves `H_cation`→`H_ion`.

### 6b. Why the suite is STILL red after 6a — four un-perceivable group nodes
With the siblings assert passing, the test reached `kinetics_check_sample_descends_to_group`, which
calls `make_sample_molecule()` on every non-product group node. Its `except` catches only
`UnexpectedChargeError` / `ImplicitBenzeneError` — an `AtomTypeError` propagates and fails the test.
`merges_necessary=False` here (2 roots, 2 reactants) and `ignore` is only the product nodes `A-`/`B+`,
so all reactant-tree nodes are sampled directly. **Four branch-99 nodes fail `make_sample_molecule`:**

| Node | Definition (branch 99) | Sampler produces | Failure |
|---|---|---|---|
| `NO_ion` | `*1 N u0 p1 c+1 {2,D}` / `O ...` | charge-on-N nitrosonium | AtomTypeError (N+, 1 double bond) |
| `Anion` | `*2 R ux px c-1` | H⁻ with 2 single bonds | AtomTypeError (H-) |
| `H_anion` | `*2 H u0 px c-1` | H⁻ with 2 single bonds | AtomTypeError (H-) |
| `O_anion` | `*2 O ux px c-1` | O⁻ with 3 single bonds | AtomTypeError (O-) |

The suite reported only `NO_ion` because it is first in file order and the exception aborts the loop.
Removing `NO_ion` alone would not green the suite — the three underspecified partner anions (`ux`/`px`
lets the sampler pick impossible valences) fail next. Greening needs repairing all four definitions:
drop `NO_ion` (consistent with holding NO+) and give the partner anions explicit `u`/`p` (as
`Plasma_Electron_Attachment`, which passes, does). **That is group-definition work beyond the
translation rule and beyond the one-pair re-nest — surfaced, not undertaken.** Per decision, the
family is held out of `input/` and this repair is a companion task.

## 7. Electron-placement resolver — never reached; no code declaration needed (verified)

The branch keys per-family electron placement in `RMG-Py-plasma/rmgpy/electron_placement.py`
(`FAMILY_ELECTRON_PLACEMENT`), and an absent family resolves to a **named failure**,
`ElectronPlacementError` — *if the resolver is invoked*. `Plasma_Charge_Transfer` is **not** in that
mapping (confirmed). Verified it is never invoked, so no declaration is needed:

- **Source:** every generated reaction takes `electrons = self.electrons` (`family.py:1781`), and
  `self.electrons = 0` for this family → generated reactions carry `electrons = 0`.
- **Sole call site:** `plasma.pyx:381` gates on `if getattr(rxn, 'electrons', 0):` — false for 0, so
  the reaction passes through by identity and `resolve_electron_placement` is never called.
- **Chemkin path:** `expand_electrons` folds an electron species only when `reaction.electrons` is
  nonzero (`chemkin.pyx:1948-1956`); for 0 it returns the lists unchanged.

So the resolver's hard-fail cannot fire for this family. (Standalone `generate_reactions` on
charged-species pairs returned 0 without the plasma-reactor context — a harness limitation, not
resolver evidence; the source-level proof above is definitive.)

## 8. Verifier

| # | Check | Result |
|---|---|---|
| 2 | Family loads alone | `electrons=0`; template `['A','B']→['A-','B+']`; **24 training reactions** with kinetics (§9) |
| 3 | Before/after `electrons` | verbatim-99 → `0`; translated → `0` (identical — finding, §1) |
| 4 | Standing suite vs baseline | baseline **1 passed** (421s); worktree WITH family in input/ **1 failed** (siblings, then the 4-node sampler, §6); delivered worktree (family held out) **at baseline / green** (§10) |
| 5 | 5 torr argon deck | `PYTHON_EXIT=0`, one `MODEL GENERATION COMPLETED`, final core **3 species / 1 reaction** — deck doesn't request this family; unaffected |
| 6 | One suite per process | separate processes throughout |
| + | Electron resolver | never reached; no `electron_placement.py` declaration needed (§7) |

## 9. Family-alone load (translated, 24 entries)

```
electrons = 0 ; reversible = True ; own_reverse = False ; reverse = Plasma_Charge_Transfer_Reverse
template reactants = ['A', 'B'] ; template products = ['A-', 'B+'] ; n_training loaded = 24
[ 1] Hp_r1 + Hm_r2 <=> H + H       A=1.132e+11 n=-0.5  Ea=0.0       rank=6 [Tanarro2015]
[ 2] H2p_r1 + Hm_r2 <=> H2 + H     A=1.204e+11 n=-0.5  Ea=0.0       rank=6 [Tanarro2015]
 ... entries 3-12 [Tanarro2015] ...
[13] O2p_r1 + O_r2 <=> O2 + Op     A=2.920e+12 n=-1.11 Ea=232839.6  rank=6 [Gupta1990]
[15] Op_r1 + N2_r2 <=> N2p + O     A=9.100e+07 n=0.36  Ea=189600.0  rank=6 [Ozawa2008]
[18] Np_r1 + N2_r2 <=> N2p + N     A=6.990e+00 n=1.47  Ea=109160.6  rank=6 [Aiken2023]
[19] Arp_r1 + N2_r2 <=> Ar + N2p   A=1.550e+07 n=0.5   Ea=0.0       rank=6 [Aiken2023]
[20] Arp_r1 + O_r2 <=> Ar + Op     A=3.850e+06 n=0.0   Ea=0.0       rank=6 [Aiken2023]
[22] O2p_r1 + N_r2 <=> Np + O2     A=8.670e+07 n=0.14  Ea=237800.0  rank=6 [Ozawa2008]
[23] O2p_r1 + N2_r2 <=> N2p + O2   A=9.880e+06 n=0.0   Ea=338400.0  rank=6 [Ozawa2008]
[24-28] {Li,Na,K,Mg,Ca}p_r1 + Hm_r2 <=> {Li,Na,K,Mg,Ca} + H        rank=9 estimated
(held: 14, 16, 17, 21 — NO+ atom-type failure)
```

(A shown SI-converted; carried values unchanged, e.g. entry 1: `1.88e-7 cm³/molecule/s × Nₐ`.)

## 10. Suite quotes

Baseline (`RMG-database-plasma/input`):
```
======================== 1 passed in 421.39s (0:07:01) =========================
BASELINE_PYTEST_EXIT=0
```
Worktree WITH family in `input/`, after the §6a re-nest:
```
======================== 1 failed in 390.21s (0:06:30) =========================
```
failing at `kinetics_check_sample_descends_to_group` → `make_sample_molecule` on `NO_ion`
(AtomTypeError). Before the re-nest it failed earlier, at the siblings assert.

Delivered worktree (family held out of `input/`):
```
======================== 1 passed in 418.68s (0:06:58) =========================
WORKTREE_HELDOUT_PYTEST_EXIT=0
```

## Disposition / files

- Translated family staged at `docs/i202-charge-transfer-carry/staged-family/Plasma_Charge_Transfer/`
  (rule edits 2/3, label renames, NO+ held, H_ion/H2_ion re-nest all applied). **Not** in `input/`.
- `recommended.py` — untouched (plasma families appear in no set; matched).
- **Companion task:** repair the four group nodes (§6b) — drop `NO_ion`; specify `u`/`p` on
  `Anion`/`H_anion`/`O_anion` — then move the family into `input/` and confirm the suite green. Also
  worth reporting the `H_ion`/`H2_ion` siblings bug upstream against branch `99`.
