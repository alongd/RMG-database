# I-041 — Are the charged-cation families reachable?

**Question.** A reaction family that loads without error and never generates a reaction is
indistinguishable, from the outside, from one that works. Which kind are the charged-cation
families?

**Answer, in one line each.**

- Charged-cation families found: **11** — not the 6 that the `Cation_*` directory prefix suggests.
  The prefix is the wrong filter; §2 enumerates by behaviour instead and shows its work.
- Families that can generate a reaction: **11 of 11.** Every one, with kinetics attached.
- Most common gate stopping the ones that cannot: **none exists at the template level.** The gate
  that does exist sits one level up and is a *supply* problem, not a template problem: all 11 need a
  cation reactant — Li⁺ for six, H⁺ for five — and no generation-time path in this database ever
  creates one. Both must be supplied as input species.

The probe was commissioned expecting the uncomfortable outcome, and did not find it at the level it
was aimed at. It found two different ones: the family set was mis-scoped (§2), and reachability is
gated on species supply rather than on the templates (§5).

---

## 1. Environment and pin

| Role | Path | State |
|---|---|---|
| Runtime (imports) | `/home/alon/Code/RMG-Py-i044-potential` | `fd1a99790`, unmodified, not rebuilt |
| Data under test | `/home/alon/Code/RMG-database-i041-reach` | branch `i041-cation-reachability`, base `b09fa27be` |

Every python invocation ran with cwd in the runtime worktree,
`PYTHONPATH=/home/alon/Code/RMG-Py-i044-potential`, and `PATH` pinned to the `rmg_env` interpreter.
No `rmgrc` was created at any worktree root.

The pin was printed as the first and last line of **every** probe script, and both confirmations hold
for all seven stages:

```
PIN-BEFORE: /home/alon/Code/RMG-database-i041-reach/input
PIN-AFTER:  /home/alon/Code/RMG-database-i041-reach/input
```

Import resolution verified independently:

```
$ cd /home/alon/Code/RMG-Py-i044-potential && PYTHONPATH=/home/alon/Code/RMG-Py-i044-potential python \
    -c "import rmgpy,os; print('rmgpy from:', os.path.dirname(rmgpy.__file__))"
rmgpy from: /home/alon/Code/RMG-Py-i044-potential/rmgpy
db: /home/alon/Code/RMG-database-i041-reach/input
```

> Note on `PYTHONPATH`. The brief's example uses `PYTHONPATH=` with `python -c`, where cwd supplies
> the import root. For a *script file* `sys.path[0]` is the script's directory, not cwd, so the bare
> `PYTHONPATH=` form raises `ModuleNotFoundError: No module named 'rmgpy'`. Setting `PYTHONPATH` to
> the runtime worktree explicitly is the same pin stated positively, and is what was used.

## 2. Enumerating the set — and why the obvious enumeration is wrong

The obvious filter is the directory prefix, and it gives six:

```
Cation_Addition_MultipleBond              Cation_NO_Ring_Opening
Cation_Addition_MultipleBond_Disprop      Cation_NO_Substitution
Cation_Li_Abstraction                     Cation_R_Recombination
```

**That filter is wrong.** It is a naming convention, not a property. Enumerating instead by what a
family *demands of a reactant* — loading all 135 family directories and asking which have a **top
template reactant fragment of net charge > 0** — gives **11**:

```
CATION FAMILIES (template requires a reactant fragment of NET charge > 0): 11
  Cation_Addition_MultipleBond                         net=+1  cation=Li   allow_charged=True  electrons=-1
  Cation_Addition_MultipleBond_Disprop                 net=+1  cation=Li   allow_charged=True  electrons=-1
  Cation_Li_Abstraction                                net=+1  cation=Li   allow_charged=True  electrons=-1
  Cation_NO_Ring_Opening                               net=+1  cation=Li   allow_charged=True  electrons=-1
  Cation_NO_Substitution                               net=+1  cation=Li   allow_charged=True  electrons=-1
  Cation_R_Recombination                               net=+1  cation=Li+  allow_charged=True  electrons=-1
  Surface_Proton_Electron_Reduction_Alpha              net=+1  cation=H+   allow_charged=True  electrons=-1
  Surface_Proton_Electron_Reduction_Alpha_vdW          net=+1  cation=H+   allow_charged=True  electrons=-1
  Surface_Proton_Electron_Reduction_Beta               net=+1  cation=H+   allow_charged=True  electrons=-1
  Surface_Proton_Electron_Reduction_Beta_Dissociation  net=+1  cation=H+   allow_charged=True  electrons=-1
  Surface_Proton_Electron_Reduction_Beta_vdW           net=+1  cation=H+   allow_charged=True  electrons=-1
```

The five `Surface_Proton_Electron_Reduction_*` families are cation families by every operational
test: `template(reactants=["Adsorbate", "Proton"], ...)` where `Proton` is the group
`1 *3 H+ u0 p0 c+1`, plus `allowChargedSpecies = True`, `electrons = -1`, and `LOSE_CHARGE` on the
cation label. They differ from the `Cation_*` six only in which cation and whether a surface site is
involved. Missing them was a scoping error, caught in adversarial review and corrected here.

### 2.1 What the net-charge test correctly rejects

A looser test — "any **top template** group containing a `c+1` atom" — returns 20 and is also wrong,
because formal charges appear inside net-neutral species. These nine are **rejected**, and rejecting
them is the right call:

```
REJECTED -- c+1 atom present but every reactant fragment is NET NEUTRAL (zwitterion/ylide):  9
  1,2_Insertion_CO          allow_charged=False electrons=0    (CO written as [C-]#[O+])
  1,3_Insertion_ROR         allow_charged=False electrons=0
  R_Addition_COm            allow_charged=False electrons=0    (CO again)
  R_Addition_CSm            allow_charged=False electrons=0    (CS as [C-]#[S+])
  Surface_Abstraction_Charge_Separation    allow_charged=False electrons=0   (N+/C- ylide)
  Surface_Abstraction_Charge_Single        allow_charged=False electrons=0
  Surface_Dissociation_Charge_Separation   allow_charged=False electrons=0
  Surface_Dissociation_Charge_Single       allow_charged=False electrons=0
  intra_NO2_ONO_conversion  allow_charged=False electrons=0    (nitro N+/O-)
```

The rejection is corroborated by a second, independent signal: **every one of the 11 accepted
families has `allow_charged_species = True` and `electrons = -1`; every one of the nine rejected has
`allow_charged_species = False` and `electrons = 0`.** Two unrelated criteria agreeing on the same
partition is what makes the count of 11 trustworthy rather than an artifact of one heuristic.

The four `Surface_*_Charge_*` families deserve a specific note because their names invite the
mistake: they *move* formal charge between atoms of a single net-neutral adsorbed ylide. They neither
consume nor produce a free cation.

### 2.2 The test is top-node — does the full tree leak?

Adversarial review raised the obvious hole: both tests above look only at the **top** template
reactant entries, and a family's *tree* can carry charged groups far below its root. Checked
directly, over every `Group` entry of all 135 families rather than only the template roots:

```
FULL-TREE: families with ANY net-positive group anywhere in the tree: 14   (top-node test gave 11)
  the 11 cation families                       allow_charged_species=True   electrons=-1
  1,2_Insertion_CO   extra   groups R_CO_R'1, R_CO_R'2      allow_charged_species=False electrons=0
  H_Abstraction      extra   groups N5_H, N5dc_H, N5dc/H/NonDeOO
                                                             allow_charged_species=False electrons=0
  R_Addition_COm     extra   group  YC.=O                    allow_charged_species=False electrons=0

FULL-TREE: families with ANY c+1 atom anywhere: 24  (4 more than the top-node c+1 test's 20:
  1,2_NH3_elimination, CO_Disproportionation, H_Abstraction, Surface_Adsorption_vdW)
```

So the leak is real but **closed by the flag, not by luck**: all three extra net-positive families
declare `allowChargedSpecies = False`, and `_create_reaction` therefore discards any reaction whose
reactants *or* products carry a net charge, before the reaction is ever returned. A net-positive
group buried in `H_Abstraction`'s tree cannot produce a cation-consuming reaction, because the
family refuses charged species outright.

The precise criterion is therefore two-part, and both parts are needed:

> **a family is cation-consuming iff a template reactant fragment can be net-positive AND the family
> declares `allowChargedSpecies = True`.**

Applied over the full tree, that criterion returns exactly the same **11**. The top-node count was
not wrong, but it was under-specified; this is the version that holds.

### 2.2 Charged but not cation-consuming

```
CHARGED BUT NOT CATION-CONSUMING: 1
  Plasma_Electron_Attachment    allow_charged=True  electrons=-1
```

Correctly outside the set: it consumes an electron and produces **anions**. The neutral `Li_*`
families (`Li_Abstraction`, `Li_Addition_MultipleBond`, `Li_NO_Substitution`,
`Li_NO_Ring_Opening`) are neutral-lithium radical families with no charged reactant and are also
outside.

## 3. What each family demands of a reactant

Every one of the 11 shares a shape: template reactant groups that split into a **cation fragment**
and a **neutral fragment**, with `reactantNum = 2`, so RMG's bimolecular path applies. The
single-`Root`-entry form used by the six `Cation_*` families is not an arity bug — `Group.split()`
returns 2 and the runtime handles it.

All 11 declare `allowChargedSpecies = True`, leave `allowChargedReactants` **undeclared** (so it
inherits `True`), and set `electrons = -1`. Consequently neither charge gate in `_create_reaction`
rejects anything here: not the two-sided `allow_charged_species` screen, nor the one-sided
`is_charged_reactant_forbidden`. `electrons = -1` is the bookkeeping partner of the `LOSE_CHARGE`
every recipe performs.

| Family | Cation | Neutral partner must be |
|---|---|---|
| `Cation_Addition_MultipleBond` | Li⁺ | any `R!H=R!H` / `#` / aromatic pair |
| `Cation_Addition_MultipleBond_Disprop` | Li⁺ | 5-atom chain `*1=*2–*4–*5–*6•` |
| `Cation_Li_Abstraction` | Li⁺ | `R–[Cl,F,H]` |
| `Cation_NO_Ring_Opening` | Li⁺ | `[O,N]` with two single bonds, **in a ring** |
| `Cation_NO_Substitution` | Li⁺ | `[O,N]` with two single bonds, **acyclic** |
| `Cation_R_Recombination` | Li⁺ | any radical `R u1` |
| `Surface_Proton_Electron_Reduction_Alpha` | H⁺ | adsorbate `R!H=X` (multiply bonded to a site) |
| `..._Alpha_vdW` | H⁺ | vdW-bound adsorbate |
| `..._Beta` | H⁺ | adsorbate `*1=*2–X` |
| `..._Beta_Dissociation` | H⁺ | adsorbate `*1–*2–X`, dissociating |
| `..._Beta_vdW` | H⁺ | vdW complex (molecule + vacant site) |

**On the two `NO` families.** `Cation_NO_Ring_Opening` and `Cation_NO_Substitution` do have
byte-identical `Root` groups and identical recipes — `git diff --no-index` on the two `groups.py`
confirms the `Root` entry and `recipe(...)` block match exactly. What separates them **as matchers**
is `productNum` (1 vs 2): breaking `*1–*2` leaves one fragment if the reactant is cyclic and two if
it is not, which is why ethylene oxide matches only Ring_Opening and dimethyl ether only
Substitution (controls in §4.2). They are *not* otherwise identical files — `template(products=...)`,
`reverse`, the `reverseMap` (present only on Ring_Opening), the subgroup trees, and `rules.py` all
differ substantially. An earlier draft said "discriminated only by productNum" and that was too
narrow.

## 4. Generation attempts and their actual output

### 4.1 Verdicts

Reactants derived from each family's **own template groups** via `Group.make_sample_molecule()`, so
the construction cannot be dismissed as hand-picked to succeed:

```
CATION FAMILY                                          DISTINCT REACTIONS   VERDICT
Cation_Addition_MultipleBond                                    1           REACHABLE
Cation_Addition_MultipleBond_Disprop                            1           REACHABLE
Cation_Li_Abstraction                                           2           REACHABLE
Cation_NO_Ring_Opening                                          1           REACHABLE
Cation_NO_Substitution                                          1           REACHABLE
Cation_R_Recombination                                          1           REACHABLE
Surface_Proton_Electron_Reduction_Alpha                         1           REACHABLE
Surface_Proton_Electron_Reduction_Alpha_vdW                     1           REACHABLE
Surface_Proton_Electron_Reduction_Beta                          1           REACHABLE
Surface_Proton_Electron_Reduction_Beta_Dissociation             1           REACHABLE
Surface_Proton_Electron_Reduction_Beta_vdW                      1           REACHABLE
```

11 of 11. The "specific gate per unreachable family" column the ticket asks for is empty by
measurement, not by omission; §4.4 records the gates that were tested for and found not to fire.

Two constructions needed care, and both are probe limitations rather than family defects:

- `Cation_NO_Ring_Opening` returns **0** from its own sample molecule, because
  `make_sample_molecule()` never builds a ring and returns water. Supplying ethylene oxide — a ring,
  which the group permits — gives 2 reactions. Recorded here rather than quietly dropped.
- `Surface_Proton_Electron_Reduction_Beta_vdW` returns 0 if either half of its vdW adsorbate is
  passed alone (`[Pt]` → 0, `C=C` → 0); merging the two fragments into one vdW complex
  (`C=C.[Pt]`) gives 1. The family's neutral side is one species that `split()` reports as two.

### 4.2 Literal generation output

Template-derived reactants (stage 7):

```
Cation_Addition_MultipleBond          c1ccccc1 + [Li+] -> 12 rxn   <=> [Li][CH]1[CH]C=CC=C1
Cation_Addition_MultipleBond_Disprop  [CH2]CCc1ccccc1 + [Li+] -> 2 <=> [Li][CH]1C=CC=CC1=C + C=C
Cation_Li_Abstraction                 Cl + [Li+] -> 2              <=> [Cl] + [LiH] ; [H] + [Li][Cl]
Cation_NO_Ring_Opening                O + [Li+] -> 0   (sample is water: no ring)
                                      C1CO1 + [Li+] -> 2           <=> [Li][O]C[CH2]
Cation_NO_Substitution                O + [Li+] -> 2               <=> [Li][OH] + [H]
Cation_R_Recombination                [H] + [Li+] -> 1             <=> [LiH]
Surface_..._Alpha                     [CH2]=[Pt] + H+ -> 1         <=> [CH3][Pt]
Surface_..._Alpha_vdW                 [PtH] + H+ -> 1              <=> [H][H].[Pt]
Surface_..._Beta                      C=[CH][Pt] + H+ -> 1         <=> C[CH]=[Pt]
Surface_..._Beta_Dissociation         C[CH2][Pt] + H+ -> 1         <=> C + [CH2]=[Pt]
Surface_..._Beta_vdW                  C=C.[Pt] + H+ -> 1           <=> C[CH2][Pt]
```

Hand-chosen realistic reactants for the six `Cation_*` families (stage 2), including negative
controls:

```
Cation_Addition_MultipleBond          C=C + Li+ -> 2   <=> [Li][CH2][CH2]
                                      CC#N + Li+ -> 2  <=> [Li]N=[C]C ; [Li]C(=[N])C
                                      C=O + Li+ -> 2 ; C=N + Li+ -> 2 ; benzene + Li+ -> 6
Cation_Addition_MultipleBond_Disprop  C=CCC[CH2] + Li+ -> 1  <=> [Li][CH2]C=C + C=C
                                      C=CC[CH2]  + Li+ -> 0   CONTROL: chain too short
Cation_Li_Abstraction                 C + Li+ -> 4 ; CCl + Li+ -> 4 ; CF + Li+ -> 4 ; CC#N + Li+ -> 3
Cation_NO_Ring_Opening                C1CO1 + Li+ -> 2 ; C1CCOC1 + Li+ -> 2 ; C1CNC1 + Li+ -> 4
                                      COC + Li+ -> 0          CONTROL: acyclic
Cation_NO_Substitution                COC + Li+ -> 2 ; CCOCC + Li+ -> 2 ; CNC + Li+ -> 6 ; CO + Li+ -> 2
                                      C1CO1 + Li+ -> 0        CONTROL: cyclic
Cation_R_Recombination                [CH3] + Li+ -> 1 ; [OH] + Li+ -> 1 ; [H] + Li+ -> 1 ; [NH2] + Li+ -> 1
                                      C + Li+ -> 0            CONTROL: u0, not u1
```

Charge and electron bookkeeping is consistent throughout all 11: `electrons = -1`, reactant net
charges `[0, +1]`, product net charges all `0`, `is_balanced() == True`.

### 4.3 Kinetics actually attach

Estimated the way `get_kinetics_from_family` does — `family.get_kinetics(rxn, rxn.template, ...)`,
using the template `generate_reactions` already stored on the reaction:

```
Cation_Addition_MultipleBond     ArrheniusChargeTransferBM  rate rules Root  k(300)=702.6  k(1000)=2.359e7
                                 ArrheniusChargeTransfer    training CH2O+Li k(300)=4.009e9
Cation_Addition_MB_Disprop       ArrheniusChargeTransferBM  rate rules       k(300)=1.184e-7 k(1000)=1377
Cation_Li_Abstraction            ArrheniusChargeTransferBM  rate rules       k(300)=14.54  k(1000)=6.157e6
                                 ArrheniusChargeTransfer    training CH4+Li  k(300)=1.078e-30
Cation_NO_Ring_Opening           ArrheniusChargeTransfer    training C2H4O+Li k(300)=2.259e7
                                 ArrheniusChargeTransfer    rate rules       k(300)=9.371e-2
Cation_NO_Substitution           ArrheniusChargeTransfer    training C2H6O-3 k(300)=1.047e-4
                                 ArrheniusChargeTransfer    rate rules       k(300)=7.926e-5
Cation_R_Recombination           Marcus                     training CH3+Li  k(300)=9.452e8
                                 Marcus                     rate rules       k(300)=9.113e8
Surface_..._Alpha                SurfaceChargeTransfer      training CH2X+H
                                 SurfaceChargeTransfer      rate rules
Surface_..._Alpha_vdW            SurfaceChargeTransfer      rate rules  Adsorbate;Proton
Surface_..._Beta                 SurfaceChargeTransfer      rate rules
Surface_..._Beta_Dissociation    SurfaceChargeTransfer      rate rules  CCX;Proton
Surface_..._Beta_vdW             SurfaceChargeTransfer      rate rules
```

Every family resolves a tree node and returns kinetics. Six of the eleven additionally match a
**training-depository** entry — i.e. the training data whose numerical content prompted this ticket
is being reached and used.

**A naming trap worth recording.** Training reaction labels write the cation as if it were neutral —
`CH3 + Li <=> CH3Li`, `CH2X + H <=> CH3X` — while the accompanying `dictionary.txt` defines that
species as charged. Verified across all 11:

```
Cation_Addition_MultipleBond/training/dictionary.txt          Li  ->  1 *3 Li u0 p0 c+1
Cation_Addition_MultipleBond_Disprop/training/dictionary.txt  Li  ->  1 *3 Li u0 p0 c+1
Cation_Li_Abstraction/training/dictionary.txt                 Li  ->  1 *3 Li u0 p0 c+1
Cation_NO_Ring_Opening/training/dictionary.txt                Li  ->  1 *3 Li u0 p0 c+1
Cation_NO_Substitution/training/dictionary.txt                Li  ->  1 *3 Li u0 p0 c+1
Cation_R_Recombination/training/dictionary.txt                Li  ->  1 *1 Li u0 p0 c+1
Surface_Proton_Electron_Reduction_Alpha/training/dictionary.txt  H ->  1 *3 H  u0 p0 c+1
```

The labels are not evidence of neutral chemistry; the adjacency lists are authoritative. Anyone
reading the training files by label alone will misread every one of these entries.

### 4.4 The end-to-end path, and the gates tested that did not fire

`rmgpy.rmg.react.react_species` — the call RMG's model enlargement makes, including
resonance-structure expansion:

```
  CC#N       + [Li+]  ->  3 rxns  ['Cation_Addition_MultipleBond', 'Cation_Li_Abstraction']
  COC        + [Li+]  ->  2 rxns  ['Cation_Li_Abstraction', 'Cation_NO_Substitution']
  [CH3]      + [Li+]  ->  1 rxn   ['Cation_R_Recombination']
  C1CCOC1    + [Li+]  ->  3 rxns  ['Cation_Li_Abstraction', 'Cation_NO_Ring_Opening']
  C=CCC[CH2] + [Li+]  ->  8 rxns  [AdditionMB, Disprop, Li_Abstraction, R_Recombination]
  CC#N       + [NH4+] ->  0 rxns  []
  CC#N       + C      ->  0 rxns  []
```

The alternative gates the ticket asks to be distinguished, each tested, each found **not** to be the
blocker:

- *Template cannot match any constructible species* — ruled out; every family matched at least one
  molecule, and for nine of eleven that molecule was derived from the family's own group.
- *Required atom types do not exist* — ruled out; `Li`, `Li+`, `H+`, and `X` all exist and build.
  (`[Na+]` does **not** build: `KeyError: 'Na'`. RMG has no sodium element, which is part of why
  these templates are element-specific rather than generically cationic.)
- *Charge / admissibility flag rejects the result* — ruled out; `allow_charged_species` and
  `allow_charged_reactants` are `True` on all 11, and `_create_reaction`'s charge screens pass.
- *Rejected downstream* — **fires partially, blocks nothing.** The global `forbiddenStructures.py`
  (33 entries, including lithium-specific `LiCONSFCl` and `LiX` forbids) rejected 2 of the 5
  `Cation_Addition_MultipleBond` products screened — `[Li]C(=[N])C` and `[Li][CH2][O]` — while the
  sibling product of the same reactant pair survived in each case. **This screen covered only the
  products actually probed; it is not a proof that every reachable channel of every family
  survives.** What it establishes is that the forbidden screen prunes some channels and eliminates
  no family.
- *Matches only reactants nothing can produce* — **this is the one that fires.** §5.

## 5. Closing the loop to reality: are the required reactants producible?

**The neutral partners are not the constraint.** Acetonitrile, ethers, alcohols, amines, alkenes,
ordinary radicals, and adsorbed C1/C2 fragments are all species RMG generates routinely.

**The cations are.** Three independent lines of evidence, for both Li⁺ and H⁺:

1. **No family creates a free cation.** `GAIN_CHARGE` appears in exactly four family recipes in this
   database — the four `Surface_*_Charge_*` families — and all four merely move formal charge within
   a single net-neutral adsorbed ylide (§2.1). None yields a free Li⁺ or H⁺. Meanwhile **sixteen**
   families carry `LOSE_CHARGE` — all 11 under test, plus `Plasma_Electron_Attachment` and the same
   four `Surface_*_Charge_*`. Charge destruction outnumbers charge creation four to one, and the
   creation that does exist is internal to a neutral species.

2. **The named reverse families do not exist as directories.** The six `Cation_*` families declare
   `reverse = Cation_Beta_Scission` / `Cation_Bond_Dissociation` /
   `Cation_NO_Ring_Opening_reverse` / `Cation_NO_Substitution_reverse`, and none of those
   directories is present. With `reversible = True` this is legitimate — the reverse rate comes from
   thermodynamics at simulation time — but it means no *generation-time* template ever emits a
   cation as a new edge species.

3. **Library reactions consume cations and never list one as a product.** Counting reaction labels:
   **36 with `[Lip]` on the reactant side, 0 on the product side**, in
   `LithiumPrimaryChargedKinetics`; `LithiumAnalogyKinetics` defines `[Lip]` but has no `[Lip]`
   reaction labels; and **9 with `proton` on the reactant side, 0 on the product side**, in
   `CO2RR_DFT_Ag111`, whose dictionary defines `proton` as `1 H u0 p0 c+1`.

   > An earlier draft of this report claimed "0 library reaction labels contain `H+` at all". That
   > was true only as a *literal string* search and was therefore worthless — it fell into exactly
   > the label/dictionary trap documented in §4.3, where a charged species is written under a
   > neutral-looking name. Corrected here. The correction *strengthens* the conclusion: the tally is
   > **45 library reactions that consume a cation, 0 that produce one.**

**What that evidence does and does not prove.** It establishes that no *generation-time* path
creates a cation, so a cation is never discovered as a new species. It does **not** prove a cation
can never appear at simulation time: those library reactions are written `<=>`, so the reverse
direction of an already-present reversible reaction can regenerate a cation that was consumed. That
is recycling of a supplied inventory, not a net source. The accurate claim is therefore *"nothing in
this database generates a cation as a new species"* — not *"nothing ever produces one"*.

**Both cations are, however, fully *supportable*.** Careful wording: a thermo, solute, or dictionary
entry does not put a species into a model — it supplies the *data* a species needs once something
else introduces it. The database contains no source term for either cation. What it does contain is
everything required for a user-supplied cation to be usable:

- Li⁺ — `[Lip]` thermo in `LithiumPrimaryThermo.py`, `Li_ion` in `computationalLithiumElectrode.py`,
  `[Li+]` solvation data in `solvation/libraries/solute.py`, and species definitions in two kinetics
  library dictionaries.
- H⁺ — species `proton` (`1 H u0 p0 c+1`) in `thermo/libraries/electrocatThermo.py` and
  `electrocatLiThermo.py`, plus `CO2RR_DFT_Ag111/dictionary.txt`.

And an input file that does exactly this exists — **outside this repo**, in the RMG-Py runtime at
`/home/alon/Code/RMG-Py-i044-potential/examples/rmg/SEI_pure_ACN/input.py`, quoted here in full for
the relevant lines because it cannot be reached from this checkout:

```python
species(label="Lip", reactive=True, structure=SMILES("[Li+]"))
...
initialConcentrations={"ACN": (0.019146,'mol/cm^3'), "Lip": (15.0,'mol/m^3')},
constantSpecies=["ACN","Lip"],
```

**Per-family producibility verdict** — identical within each cation group, because the constraint is
the cation they share:

| Families | Neutral partner producible? | Cation generated by RMG? | Cation *supported* by the database? | Reachable in practice? |
|---|---|---|---|---|
| the six `Cation_*` | yes | **no** | yes — thermo, solute, electrode, library entries | yes, when Li⁺ is an input species |
| the five `Surface_Proton_Electron_Reduction_*` | yes | **no** | yes — `proton` thermo + `CO2RR_DFT_Ag111` entries | yes, when H⁺ is an input species |

Supplying the cation is **necessary**. It is not by itself **sufficient**: the family must be in
`kineticsFamilies`, the cation must be `reactive=True`, products must clear
`generatedSpeciesConstraints` and the forbidden screen, thermo must exist for each product, and flux
filtering must not prune the reaction. Those model-level conditions were not exercised (§6), and the
word "iff" would overstate what was measured. The SEI input file above satisfies each of them by
inspection — it lists the families, marks `Lip` reactive, and constrains the product space — but no
model was actually run here, so that is a reading of the input file, not a demonstration.

**Which is the case that matters for the plasma line of work.** The six `Cation_*` families are
lithium templates and the five `Surface_*` families are proton templates; none is a generic cation
template. In a plasma mechanism whose cations are `N2+`, `Ar+`, `H3O+`, `CH3+`, `C2H5+`, `NH4+`,
each of those **six** cations was built and tried against every neutral in §4.2, for every family,
and every combination returned **N=0 without exception**. `H+` fires only in the surface families and
only against an adsorbate on a metal site — it produces nothing in the gas phase. (A seventh control,
`[Na+]`, could not be tried at all: RMG has no sodium element.) Whether that is a gap to fill or a
correct scope boundary is a chemistry decision outside this ticket.

## 6. What this probe did *not* establish

Stated plainly, because a reachability verdict is easy to over-read:

- **`generate_reactions` and `react_species` prove template emission, not model contribution.** They
  bypass or under-test: family selection from the input file, `reactive` flags,
  `generatedSpeciesConstraints` (`maximumCarbonAtoms`, `maximumRadicalElectrons`, …), thermo and
  solvation availability for every product, `filterReactions` and flux-based pruning, duplicate
  merging, and seed/library precedence. A family that emits a reaction here can still contribute
  nothing to a converged model.
- **The forbidden-structure screen covered only the probed products**, not the full reachable
  product space of any family.
- **Charge-transfer kinetics were evaluated at the default potential** (`V0 = 0 V`). The
  `ArrheniusChargeTransfer`, `Marcus`, and `SurfaceChargeTransfer` models returned finite `k(T)`
  under that default; whether they behave correctly under the electrode potentials a real
  electrochemical reactor imposes was not tested.
- **No full RMG model enlargement was run** — no `rmg.py` job, no reactor, no convergence. The
  ticket asked whether reactions come out of the families; that is what was measured.

**Provenance of the runtime-dependent claims.** Everything in §4 — which reactions are emitted, which
templates resolve, which kinetics attach, which training entries are hit — is behaviour of the RMG-Py
runtime and **cannot be checked by reading this repository alone**. It is reproducible only by
re-running the stage scripts against `/home/alon/Code/RMG-Py-i044-potential` with the pin in §1. The
captured stdout/stderr of all eight stages live under
`/tmp/claude-1000/.../scratchpad/stage{1..8}.{stdout,stderr}.log`; being in a scratch directory they
are not durable, and the quoted excerpts in this report are the durable record. Claims that *are*
checkable from this repo alone — the enumeration, every count, the group and dictionary contents —
are marked as such by quoting the files.

The honest summary: **every one of the 11 families emits reactions and gets kinetics; whether each
survives into a converged model is a further question this probe did not answer.**

## 7. Read-only compliance

No family, group, template, training entry, rate rule, or RMG-Py module was modified. Nothing at the
template level was found to be broken, so the temptation the ticket warned about did not
materialise. Two observations that *could* invite an edit, recorded rather than acted on:

- **Would change:** widen the cation atom in the six `Cation_*` `Root` groups from `Li` to a
  charged-atom wildcard. **Predicted effect:** the families would fire for any `c+1` species RMG can
  build, turning a lithium mechanism into a generic-cation one. **Predicted problem:** every rate
  rule and training entry beneath those roots was fitted to lithium, so a wildcard would silently
  apply Li⁺ kinetics to `N2+` and `CH3+`. A chemistry decision, not a probe decision; not made here.
- **Observation, not a finding:** `C=C + [Li+] <=> [Li][CH2][CH2]` yields a product written with two
  separate radical sites. Whether that is the intended electronic state is a chemistry question the
  ticket explicitly excludes.

## 8. Method, and probe bugs found along the way

Seven scratch probe scripts, all outside both tracked trees, under
`/tmp/claude-1000/.../scratchpad/`, each with stdout and stderr persisted:

| Stage | What it did |
|---|---|
| 1 | Enumerate `Cation_*`; dump flags, template, split fragments, recipe |
| 2 | Every `Cation_*` family × candidate neutrals × 9 cations; `generate_reactions` |
| 3 | Forbidden-structure screen; first (failed) kinetics attempt |
| 4 | Kinetics via the stored template; per-family tally |
| 5 | Corrected `get_kinetics` unpacking; end-to-end `react_species` |
| 6 | Adversarial review → enumerate by behaviour over all 135 families |
| 7 | Enumerate by **net charge**; probe all 11 with template-derived reactants |
| 8 | Second adversarial review → re-enumerate over the **full group tree**, not just template roots |

Four probe bugs were found and fixed rather than reported as family defects. They matter because
each produced convincing-looking output that would have supported a *wrong* verdict:

1. `Molecule` rejects ad-hoc attributes (cython slots) — cosmetic, caught immediately.
2. `get_reaction_template` cannot re-derive a template from a reaction whose atom labels
   `generate_reactions(delete_labels=True)` has already stripped. This raised
   `UndeterminableKineticsError` for all six families in stage 3 — a textbook false "unreachable".
3. `get_kinetics` returns a **list** of `[kinetics, source, entry, is_forward]`, not a 2-tuple.
4. `make_sample_molecule()` never builds a ring, so `Cation_NO_Ring_Opening` looked dead until a ring
   was supplied by hand (§4.1).

Three corrections came from adversarial review rather than from the probe itself, and they are worth
naming because each was a case of the report asserting more than it had measured:

1. **The enumeration error in §2** — using the `Cation_*` name prefix instead of a behavioural test.
   Largest single correction: the family set went from 6 to 11.
2. **The top-node blind spot** (§2.2) — the behavioural test looked only at template roots. Checking
   the full tree found three more families with net-positive groups; all three are blocked by
   `allowChargedSpecies = False`, so the count of 11 survives, but only once the flag is made part of
   the criterion rather than a coincidence.
3. **The `H+` string search** (§5) — "0 library reaction labels contain `H+`" was literal-string
   blindness to `CO2RR_DFT_Ag111`'s nine `proton` reactions, in a report that documents that exact
   trap two sections earlier.
