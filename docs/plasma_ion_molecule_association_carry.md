# Carrying `Plasma_Ion_Molecule_Association` from branch `99` — outcome

**Ticket:** I-203. **Worktree:** `/home/alon/Code/RMG-database-i203-ionmolecule` (branch
`i203-ionmolecule`, cut from `plasma`, 0 behind). **Code repo (read-only):**
`/home/alon/Code/RMG-Py-plasma` @ `4910d8c52`. **Rule applied:**
`/home/alon/Code/RMG-database-i200-collisional/docs/plasma_family_carry_translation_rule.md`.

## Verdict

The translation rule was applied and is **correct and complete** for this family — the translated
files load, the family reports the right template, the right `electrons`, and all three training
reactions with their kinetics intact. **But the family does not land in `input/`**: it has a
per-family blocker beyond the rule's scope (like the pathfinder's `NO+` and spectator blockers for
`Plasma_Collisional_Ionization`). Its `FORM_BOND` recipe, carried **byte-identical** from `99`,
is incompatible with this branch's `apply_recipe`, so the family cannot generate its own sample
reactions and turns the standing kinetics suite red. The translated files are staged under
`docs/plasma_ion_molecule_association_staged/`; re-landing is a move once the recipe question
(a gated species/reaction-semantics change) is resolved.

## Questions 1–3 (probes)

### Q1 — what the rule implies for THIS family

This family's template is `template(reactants=["A","B"], products=["AB+"], ownReverse=False)` with
`product_electrons = 0` and `custom_kinetics = False`. The reaction is `A+ + B (+M) <=> AB+ (+M)` —
an ion associates with a neutral; **charge is conserved and no free electron is produced or
consumed**. So, per the rule's five edits:

1. Strip `e-` from the template → **no-op** (there is no `e-`; unlike the five families the rule was
   worked against, this one never lists an electron as a template species).
2. Delete `custom_kinetics = False` → done (loader never reads it; `family.py` has no read).
3. `product_electrons = 0` → `electrons = 0`. Sign reasoning: forward produces 0 free electrons,
   consumes 0, net **0**. This is also the loader's seeded default (`family.py:675`), so **for this
   family the electron edit is a formal rename with no behavioural change** — verbatim-99 and
   translated both yield `electrons = 0` (measured below). The rule's usual crux (a silent
   `electrons` mismatch) is therefore trivial here.
4. `training/dictionary.txt`: no `e-` entry to remove; rename charged labels
   `Li+→Lip, LiH+→LiHp, Na+→Nap, NaH+→NaHp, Mg+→Mgp, MgH+→MgHp` (`H` neutral, unchanged);
   adjacencies verbatim.
5. `training/reactions.py`: labels rewritten to the renamed species; kinetics/rank/desc verbatim.

`rules.py` carries verbatim. The `diff 99 → translated` is exactly these edits and nothing else.

**A note the rule does not anticipate:** here the reason a verbatim `99` copy is unusable is *not*
the electron bookkeeping (which is `0` either way) but edits 4–5. The `99` training labels
(`Li+ + H <=> LiH+`) carry a `+` inside the species name that the depository label parser reads as
the reactant separator, so a verbatim copy fails to load its training set:
`DatabaseError: Species Li ... missing from its dictionary` (measured below).

### Q2 — the two structural walls (both expected NOT to apply; confirmed)

**(a) Atom-type perception.** All seven training species perceive cleanly on this branch (probe
`Molecule().from_adjacency_list` for each):

```
OK   Li+    atomtypes=['Li+']        fragments=1
OK   H      atomtypes=['H0']         fragments=1
OK   LiH+   atomtypes=['Li+', 'H0']  fragments=2
OK   Na+    atomtypes=['Na+']        fragments=1
OK   NaH+   atomtypes=['Na+', 'H0']  fragments=2
OK   Mg+    atomtypes=['Mg+']        fragments=1
OK   MgH+   atomtypes=['Mg+', 'H0']  fragments=2
```

The products `LiH+/NaH+/MgH+` are disconnected two-fragment species in the `99` dictionary (no bond
line), but they perceive without error. Wall (a) does not apply.

**(b) Spectator.** The template has no species appearing unchanged across the arrow (A and B both
merge into AB+); the rule itself names `Plasma_Ion_Molecule_Association` among the five families
with no molecular spectator. `kinetics_check_groups_nonidentical` is not tripped. Wall (b) does not
apply.

### Q3 — the training set

Three entries travel (Li+/Na+/Mg+ each + H), with kinetics, rank (9), `shortDesc`
(`estimated`) and `longDesc` carried unchanged. No number was invented, refit or improved.

## Verifier evidence

### V1 — family loads alone (translated files, worktree DB)

```
family            : Plasma_Ion_Molecule_Association
template reactants: ['A', 'B']
template products : ['AB+']
electrons         : 0
reverse           : cation_dissociation
n training entries: 3
  [1] Lip + H <=> LiHp   Arrhenius(A=(60200,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), ...)   rank=9 'estimated'
  [2] Nap + H <=> NaHp   Arrhenius(A=(1.02e+08,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), ...) rank=9 'estimated'
  [3] Mgp + H <=> MgHp   Arrhenius(A=(602000,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), ...)   rank=9 'estimated'
```

### V2 — electron bookkeeping before/after

```
[TRANSLATED]  electrons = 0
[VERBATIM-99] electrons = 0   (product_electrons=0 in file is ignored; seeded default sticks)
              — and verbatim-99's FULL load stops at the training set:
                DatabaseError: Species Li ... missing from its dictionary  (the '+' label collision)
```

Both `0`, as predicted. `electrons` is read during the groups exec (`family.py:696`), before the
training depository load (`family.py:789`) that fails on the verbatim labels.

### V3 — standing kinetics DB test (`databaseTest.py::TestDatabase::test_kinetics`, one suite per process)

```
baseline DB (RMG-database-plasma/input)                 : 1 passed  in 410.35s
worktree DB, family IN input/                           : 1 FAILED  in 371s   (kinetics_check_sample_can_react)
worktree DB, family staged OUT of input/ (final state)  : 1 passed  in 393.92s
```

Landing the family turns the suite red; removing it restores green, == baseline. **The family was
the sole cause of the red.**

**Cause (diagnosed, not assumed).** `kinetics_check_sample_can_react` calls `apply_recipe` on the
family's own sampled reactants (`H+/Li+/Na+/Mg+ each + H`); all four return `None`. DEBUG logging
pins the gate at `family.py:1585` (charge balance): reactant net charge 1, **product net charge 2**.
The mechanism, for `Li+ + H`:

- recipe = `[['LOSE_RADICAL','*2',1], ['FORM_BOND','*1',0,'*2']]` — deradicalises H (u1→u0) and
  forms an **order-0 (van der Waals) bond** between `*1` and `*2`.
- `apply_recipe` calls `remove_van_der_waals_bonds()` (`family.py:1535`) **before** charge
  accounting, stripping that bond; then `update_charge()` (`family.py:1557`).
- The now-bare H (u0, no real bond, no radical) is re-read as **H⁺**. Product becomes `[Li⁺]·[H⁺]`,
  net **+2**, vs reactant net +1 → charge imbalance → `None`.

Measured charge evolution:

```
after recipe (order-0 bond present):        Li u0 c+1 bonds=1 | H u0 c+0 bonds=1 | net +1
after remove_van_der_waals_bonds+update:    Li u0 c+1 bonds=0 | H u0 c+1 bonds=0 | net +2   <- product
apply_recipe: H+ + H -> None | Li+ + H -> None | Na+ + H -> None | Mg+ + H -> None
```

The recipe is **byte-identical to `99`** (verified). This is a genuine `99`→`plasma` recipe
incompatibility surfacing on the target branch — not a false positive in the check (the family
truly cannot make its own reaction here), and not introduced by the translation (label/electron
edits do not touch the recipe). Forcing `electrons = 1` would make the charge "balance" arithmetic
pass but is scientifically wrong (no electron is produced) and would still leave the product as
`[Li⁺]·[H⁺]` rather than `LiH⁺` — i.e. building to pass the check, which the doctrine forbids.

The honest fix is a recipe change (a real covalent `FORM_BOND` order and matching radical
bookkeeping so the product is a bonded `LiH⁺`), which is a **gated** change to the family's
reaction/matching semantics and outside this database-only carry. Held for a decision.

### V4 — 5 torr argon deck (worktree DB, canonical deck, clean run dir)

`docs/i194-ar5torr-plasma-lineage/input.py`, `PYTHON_EXIT` captured from the interpreter:

```
PYTHON_EXIT=0
one "MODEL GENERATION COMPLETED"
final model core: 3 species / 1 reactions   (Ar + e- => Arp + 2 e-, via PlasmaArgon)
```

The deck names `kineticsFamilies=['Plasma_Electron_Attachment']` only and never requests this
family, so it is unaffected whether or not the family is present; the run confirms the branch itself
is healthy.

### V5 — electron-placement resolver is never reached (per-owner declaration NOT needed)

The branch carries a per-owner electron-placement registry
(`RMG-Py-plasma/rmgpy/electron_placement.py`, `FAMILY_ELECTRON_PLACEMENT`, keyed by owner label,
valued `(reactant_count, product_count)`). An owner absent from it resolves to a **named failure**,
`ElectronPlacementError`, never a net-derived guess. `Plasma_Ion_Molecule_Association` is absent.
Verified (not assumed) that it does not need to be present:

```
built reaction     : Lip + H <=> LiHp   (family=Plasma_Ion_Molecule_Association, electrons=0)
reactor gate expr  : bool(getattr(rxn,'electrons',0)) = False
=== through the REAL reactor gate (_resolve_electron_placements, plasma.pyx:378-383) ===
resolver invocations: 0
reaction passed through by identity: True
=== resolver called DIRECTLY (bypassing the gate) ===
ElectronPlacementError: Family 'Plasma_Ion_Molecule_Association' has no electron-placement
  declaration ...; refusing to infer electron placement from the net electron count.
```

- The reactor only calls `resolve_electron_placement` for reactions with **nonzero** `electrons`
  (`plasma.pyx:379`). This family's reaction carries `electrons = 0`, so the gate is falsy and the
  resolver is **not invoked** (0 calls, reaction passed through by identity).
- The gate is load-bearing: called directly, the resolver **does** raise `ElectronPlacementError`
  naming the family. So "never reached" is exactly what makes the absent declaration correct —
  matching the module's own docstring (electron_placement.py:193-197).
- Independently, the family cannot generate any reaction on this branch at all (V3's `apply_recipe`
  blocker), so nothing from it ever reaches the reactor in the first place.

No `ElectronPlacementError` arises in the live path; **no companion code-repo declaration is
needed**, and `electron_placement.py` was not edited.

## Disposition

- Translated files staged at `docs/plasma_ion_molecule_association_staged/` (`groups.py`,
  `rules.py`, `training/dictionary.txt`, `training/reactions.py`).
- Family **not** added to `input/`; **not** added to any set in `recommended.py`.
- Re-landing = move the four files back into
  `input/kinetics/families/Plasma_Ion_Molecule_Association/` once the recipe (gated) is fixed so
  `apply_recipe` yields a bonded `AB⁺` with balanced charge.
