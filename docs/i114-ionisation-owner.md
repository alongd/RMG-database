# I-114 — Who owns electron-impact ionisation?

**Question.** The electron-placement declaration was widened from `(side, count)` to
`(reactant_count, product_count)`, so `Li + e⁻ → Li⁺ + 2e⁻` became expressible. Nothing declared
it. Should a **reaction family** or a **kinetics library** own it, and does the whole path
resolve once something does?

**Answer, in one line each.**

- **Owner: a library** — `input/kinetics/libraries/PlasmaElectronImpactIonization`, one entry,
  `[Li] => [Lip]`, `electrons = +1`, irreversible, kinetics `VoronovEIArrhenius(Z=3, N=3)` read
  from the shipped table.
- **Why not a family:** RMG cannot build a rate-rule tree out of Voronov fits at all — both
  averaging implementations crash on the type (§4.2) — so a Voronov family is capped at one
  training entry per node forever. Its generativity, the only thing a family buys, is zero.
- **Coverage of the fits:** 13 elements / 134 `(Z, N)` stages in the table; **7** elements RMG
  can build both endpoints for (H, He, Li, N, O, Si, Ar); **1** whose product cation this
  database has monatomic thermochemistry for (Li⁺). §3.
- **A species the fits do not cover gets *nothing*** — no match, no estimate, no rate. A library
  has no matcher. §6.
- `Li + e⁻ → Li⁺ + 2e⁻` **loads, balances, resolves placement, and is accepted by
  `PlasmaReactor`**, each shown separately in §5, with `kf` equal to the Voronov coefficient at
  the reactor's Tₑ to 12 significant figures.

**The premise this ticket was expected to rest on turned out to be wrong**, and saying so is part
of the answer: the anticipated objection to a family — "the template will match more than its
data supports" — does not hold here (§4.1). The real objection had to be found somewhere else.

Evidence labels: **[R]** code (file:line) · **[D]** database (file, entry) · **[M]** measured
(command and output shown) · **[L]** literature · **[I]** inference with its basis.

---

## 1. Environment and pin

| Role | Path | State |
|---|---|---|
| Reference runtime, as briefed | `/home/alon/Code/RMG-Py-i113-placement-widening` | `dde602778`, branch `i113-placement-widening`, unmodified, **not rebuilt** (see below) |
| Runtime carrying the declaration | `/home/alon/Code/RMG-Py-i114-ionisation-declaration` | branch `i114-ionisation-declaration`, `4a5bcba03`, forked from `dde602778` |
| Data under test | `/home/alon/Code/RMG-database-i114-ionisation` | branch `i114-ionisation-declaration`, base `fb3c13c60` |
| Interpreter | `/home/alon/anaconda3/envs/rmg_env/bin/python` | 3.9.23 |

The registry line lives in RMG-Py and cannot ship from a database repository, so it went on its
own branch forked off the reference one rather than into another ticket's worktree. §4 was
measured against the reference runtime, before that branch existed; §5 was re-run against the
branch with the entry **shipped**, no runtime injection. That worktree carries no compiled
extensions of its own — the 104 built `.so` files were copied across from the reference worktree,
which is sound because the two trees differ only in `electron_placement.py`, and that module is
pure Python with no `.so`. No `make` of any kind was run.

**[M]** Import resolution, printed before any other work:

```
$ PATH=/home/alon/anaconda3/envs/rmg_env/bin:$PATH \
  PYTHONPATH=/home/alon/Code/RMG-Py-i113-placement-widening \
  python -c "import sys,rmgpy;print('py:',sys.executable);print('rmgpy:',rmgpy.__file__)"
py: /home/alon/anaconda3/envs/rmg_env/bin/python
rmgpy: /home/alon/Code/RMG-Py-i113-placement-widening/rmgpy/__init__.py

$ python -c "from rmgpy.electron_placement import FAMILY_ELECTRON_PLACEMENT as F; print(F)"
{'Plasma_Electron_Attachment': (1, 0), 'Cation_R_Recombination': (1, 0)}

# and on the branch carrying the declaration:
$ PYTHONPATH=/home/alon/Code/RMG-Py-i114-ionisation-declaration python -c \
    "import rmgpy.electron_placement as ep; print(ep.__file__); print(ep.FAMILY_ELECTRON_PLACEMENT)"
/home/alon/Code/RMG-Py-i114-ionisation-declaration/rmgpy/electron_placement.py
{'Plasma_Electron_Attachment': (1, 0), 'Cation_R_Recombination': (1, 0),
 'PlasmaElectronImpactIonization': (1, 2)}
```

The two-element tuples confirm the **widened** declaration is the one in play; the superseded
`(side, count)` spelling would have read `('reactants', 1)`.

**On building.** The reference branch did **not** need building, checked rather than assumed
**[M]**: every compiled extension is newer than every source. `reaction.py`, `arrhenius.pyx` and
`plasma.pyx` were all last written at `21:20:46`; their `.so` files were built at `21:25`–`21:27`.
The widening commit (`21:45`) touched only `rmgpy/electron_placement.py`, which is pure Python and
is not cythonized. No `make` of any kind was run.

**`database.directory`** is pinned to **this** worktree, never the shared plasma checkout. The
`rmgrc` shipped on the runtime branch points at `../RMG-database-plasma/input` **[R]**
(`RMG-Py-i113-placement-widening/rmgrc`), so leaving the pin to discovery would have measured a
database nobody edited. Every probe prints `PIN-BEFORE` / `PIN-AFTER` and both read
`/home/alon/Code/RMG-database-i114-ionisation/input` in all six stages. The suite pins the same
way, in `test/conftest.py`.

---

## 2. What the decision actually turns on

A family is generative: a template matches and RMG produces reactions for species it has never
seen. A library is exact: named reactions, named rates, no matching. The question is therefore
not "which is more powerful" but **"is there generativity to be had here, and what does buying it
cost?"**

Three things bear on that, and all three were checked rather than assumed.

---

## 3. Species coverage of the existing fits — as a number and a list

**[D]** `input/kinetics/voronov.yaml` — Voronov, G. S. (1997), *Atomic Data and Nuclear Data
Tables* **65**(1), 1–35, "A practical fit formula for ionization rate coefficients of atoms and
ions by electron impact: Z = 1–28" **[L]**.

**[M]** Parsed directly:

```
Voronov blocks: 13, total (Z,N) stages: 134
elements: [(1,'H',1), (2,'He',2), (3,'Li',3), (6,'C',6), (7,'N',7), (8,'O',8), (11,'Na',11),
           (12,'Mg',12), (13,'Al',13), (14,'Si',14), (18,'Ar',18), (19,'K',19), (20,'Ca',20)]
Neutral->+1 stages present: 13   (exactly one per element)
```

So: **13 elements**, **134 ionisation stages**, of which **13** are the neutral → +1 stage. The
other **121 are ion → higher-ion** stages (Li II → Li III, C V → C VI, …). Those need multiply
charged species, which is a separate representational problem this ticket does not open.

**[M]** How many of the 13 can RMG build, in their gas-phase ground states, on *both* sides?

```
sym  neutral                        cation
H    OK q=+0 [H]                    OK q=+1 [H+]
He   OK q=+0 [He]                   OK q=+1 [He+]
Li   OK q=+0 [Li]                   OK q=+1 [Li+]
C    OK q=+0 [C]                    FAIL AtomTypeError (C u1 p1 c+1)
N    OK q=+0 [N]                    OK q=+1 [N+]
O    OK q=+0 [O]                    OK q=+1 [O+]
Na   FAIL KeyError: 'Na'            FAIL KeyError: 'Na'
Mg   FAIL KeyError: 'Mg'            FAIL KeyError: 'Mg'
Al   FAIL KeyError: 'Al'            FAIL KeyError: 'Al'
Si   OK q=+0 [Si]                   OK q=+1 [Si+]
Ar   OK q=+0 [Ar]                   OK q=+1 [Ar+]
K    FAIL KeyError: 'K'             FAIL KeyError: 'K'
Ca   FAIL KeyError: 'Ca'            FAIL KeyError: 'Ca'

Physical ground states both buildable: 7 -> ['H', 'He', 'Li', 'N', 'O', 'Si', 'Ar']
```

**7 of 13.** Na, Mg, Al, K and Ca raise `KeyError` — RMG has no atom types for them, the same wall
`docs/i041-cation-reachability.md` §4.4 hit with `[Na+]`. C⁺ as `C u1 p1 c+1` raises
`AtomTypeError`. These are runtime limits, not database omissions: **a family could not have
reached them either.**

**[D]** Of those 7, how many have thermochemistry for the product cation as a *free monatomic
ion* in this database? Grepping every `thermo/libraries/*.py` for a single-line adjacency list
carrying `c+1` returns exactly two species:

| species | file | entry |
|---|---|---|
| `[Lip]` = `1 Li u0 p0 c+1` | `LithiumPrimaryThermo.py` (index 65), `computationalLithiumElectrode.py` | Li⁺ |
| `1 H u0 p0 c+1` | `electrocatThermo.py`, `electrocatLiThermo.py` | `proton` |

Every other `c+1` hit is a *bonded* atom inside a polyatomic species (NO⁺, NH₄⁺, …), not a free
cation. **[I]** The `proton` entry is an electrocatalysis reference species — it appears alongside
`CO2RR_DFT_Ag111` and the Li-electrode libraries — so putting it in a gas-phase plasma would
import an unrelated reference state. Basis: the libraries it lives in and their contents; it is a
judgement about reference states, not a measurement.

**So coverage narrows 13 → 7 → 1**, and the one is Li — which is also the species this whole line
of work is aimed at. He⁺, N⁺, O⁺, Si⁺ and Ar⁺ have no monatomic thermochemistry here at all; until
that lands, no owner of any kind could put those reactions into a model.

---

## 4. Family or library

### 4.1 The expected objection, and why it is wrong

The objection this project has been bitten by, and the one this ticket warned about, is *a
template that matches more than its data can support*. Applied here it reads: a single-atom
ionisation group would match that element's atom **inside arbitrary molecules** and hand them the
free-atom Voronov rate.

**[M]** Checked before building anything on it, by asking RMG which molecules the candidate
ground-state groups actually match:

```
Li_atom_u1p0c0   matches  1/18 : Li atom(1)
Ar_u0p4c0        matches  1/18 : Ar atom(1)
N_u3p1c0         matches  1/18 : N atom(1)
O_u2p2c0         matches  1/18 : O atom(1)
any_atom_R       matches 12/18 : LiH(2), LiOH(2), CH3Li(5), Li2(2), NH3(3), HCN(2),
                                 CH3NH2(6), H2O(2), CH3OH(5), OH(1), CH4(5), benzene(12)
```

(18 test molecules: the free atoms plus LiH, LiOH, CH₃Li, Li₂, N₂, NH₃, HCN, CH₃NH₂, O₂, H₂O,
CH₃OH, OH, CH₄, benzene. The `any_atom_R` row is the positive control showing the matcher is live
and that a *loose* group does leak everywhere.)

**The premise is refuted.** A ground-state atom's `(u, p, c)` signature is unique to the
**unbonded** atom: bonding an atom consumes its unpaired electrons, so `Li u1 p0 c0` cannot match
the Li of CH₃Li (`u0`), and `Ar u0 p4 c0` cannot match anything bonded at all. A per-element
ionisation group is naturally exact.

This matters twice over. It removes the argument I expected to make, and it means a family here
would *not* have been unsafe — so rejecting one has to be justified by cost and by what it buys,
not by danger.

### 4.2 What actually kills the family: RMG cannot average Voronov fits

Every trained family runs `fill_rules_by_averaging_up` **[R]** (`family.py:3813`, and directly in
the attachment family's own test fixture). When a tree node has more than one child carrying a
rule, that walks into `KineticsRules._get_average_kinetics` **[R]** (`rules.py:236`).

**[M]** Fed the two Voronov fits the table gives for Li and Ar:

```
-- averaging two Voronov fits, the step every trained family runs --
  rules._get_average_kinetics   -> AttributeError: 'rmgpy.kinetics.arrhenius.VoronovEIArrhenius'
                                   object has no attribute 'n'
  family.average_kinetics       -> UnboundLocalError: local variable 'kinetics' referenced
                                   before assignment
```

Both refuse, for the same underlying reason: **[R]** `family.average_kinetics` (`family.py:4814`)
guards on a closed allowlist —

```python
if type(kinetics_list[0]) not in [Arrhenius, SurfaceChargeTransfer, ArrheniusChargeTransfer, Marcus]:
    raise Exception('Invalid kinetics type {0!r} for {1!r}.'.format(type(kinetics), self))
```

— and `VoronovEIArrhenius` is not on it. (That guard is itself broken: it names `kinetics` and
`self`, neither of which exists in that scope, so it raises `UnboundLocalError` instead of its own
message. Recorded, not fixed — it is an RMG-Py defect and this is a database ticket.) The
`rules.py` sibling has no type guard at all and simply reaches for `.n`, which a Voronov fit does
not have.

**[I]** The consequence: a Voronov-trained family is limited to **one training entry per node,
forever**. The moment a second element is trained under the same root, the family stops loading.
That is not a family, it is a library with template machinery bolted on, and it fails in a way
that looks like a regression. Basis: the two measured exceptions plus the call site at
`family.py:3813`.

### 4.3 The three costs a family would carry anyway

**Zero generativity by construction.** The only safe family shape here is the
`Plasma_Electron_Attachment` pattern **[D]** — a `LogicOr` root whose members are exactly its own
L2 children, so `descend_tree` can never stop at the root's averaged rule. That family's own
`groups.py` states the reason in terms that transfer verbatim: *"there is no group-additivity
trend to interpolate along, so an 'estimate' produced by averaging these three entries is not an
uncertain number, it is a fabricated one."* Ionisation is worse, not better: the Voronov fit is
per-stage in **five** parameters (A, P, X, K and the threshold dE), and dE is the species'
ionisation potential — a physical constant of that species, not something a group tree can
interpolate. A family built this way matches exactly the species it has data for, which is exactly
the set of entries a library would list.

**Two recipes, so two families.** **[I]** A family has one recipe. The 7 buildable elements split
into two recipe classes by their ground-state electron configuration:

| recipe | elements | example |
|---|---|---|
| `LOSE_RADICAL` | H, Li, N, Si | `Li u1 p0 c0` → `Li u0 p0 c+1` |
| `LOSE_PAIR` + `GAIN_RADICAL` | He, O, Ar | `Ar u0 p4 c0` → `Ar u1 p3 c+1` |

(Basis: the ground-state adjacency lists in §3 and RMG's recipe-action vocabulary **[R]**,
`family.py:349–360`. Open-shell atoms give up an unpaired electron; closed-shell ones must break a
lone pair, leaving an unpaired electron behind.) So even the degenerate zero-generativity family
would have to be *two* families to span the coverage — for seven reactions, six of which cannot
enter a model for want of thermochemistry.

**Direction.** A binding ruling requires forward and reverse to be represented explicitly as
separate one-way processes, and forbids treating the reverse of a process as the same channel run
backwards. Families are built around `reversible` and a named `reverse` template; a library entry
written `=>` is one-way by construction and nothing can silently reverse it. `PlasmaReactor`
enforces the same policy independently **[R]** (`plasma.pyx:508`, `NonEquilibriumReverseRateError`
for any reversible electron-temperature-dependent reaction), so a reversible entry could not have
run regardless.

### 4.4 What would have changed my mind

Stated positively, so the decision can be reopened on evidence rather than taste:

1. **A Voronov-shaped rate law that RMG can average**, or a `VoronovEIArrhenius` entry in
   `average_kinetics`'s allowlist with a defensible averaging rule for dE. There is no defensible
   rule — an averaged ionisation potential is not one — so this would have to arrive as physics,
   not as a code change.
2. **Molecular ionisation data.** The plasma species that actually matter (N₂, CH₄, Ar in a
   molecular mix) ionise through cross-sections that depend on electronic structure, and Voronov
   covers atoms and ions only. A fitted set spanning a *homologous series* — where a group tree
   could express what varies — would be the first real argument for a template.
3. **Coverage crossing the point where enumeration hurts.** At 1 usable species, and 7 in the best
   case, the entry list is shorter than the group tree. At tens or hundreds it would not be.

None of the three holds today. If any starts to, this decision should be revisited — and the
library is a strictly easier thing to migrate *from* than a family with a trained tree is.

---

## 5. The whole path, step by step

**[M]** Run against the pinned worktrees. Steps 1–4 are the four the ticket asks to see
separately; each is also a test in `test/test_plasma_electron_impact_ionization.py`.

### Step 1 — LOAD

```
INFO:root:Loading kinetics library PlasmaElectronImpactIonization from
  /home/alon/Code/RMG-database-i114-ionisation/input/kinetics/libraries/PlasmaElectronImpactIonization/reactions.py...
library loaded  : PlasmaElectronImpactIonization  entries: 1
entry.label     : [Li] => [Lip]
reaction class  : LibraryReaction | library = PlasmaElectronImpactIonization
                                  | family  = PlasmaElectronImpactIonization
reactants       : [('[Li]', 0)]
products        : [('[Lip]', 1)]
rxn.electrons   : 1
rxn.reversible  : False
kinetics        : VoronovEIArrhenius | A = 8.37078e+16 cm^3/(mol*s) | dE = 5.4 eV | electrons = 1.0
explicit electron participants: 0
```

The kinetics are **not authored here**: the entry is `VoronovEIArrhenius(Z=3, N=3)`, which reads
`settings['database.directory']/kinetics/voronov.yaml` at load **[R]** (`arrhenius.pyx:1541`), so
the shipped table stays the single source of the numbers. `electrons = +1` arrives on the reaction
because `KineticsLibrary.load` copies it off the rate law **[R]** (`library.py:583`).

### Step 2 — BALANCE

```
rxn.is_balanced() : True
net charge L/R    : +0 / +1   (electrons=+1 closes it)
```

Atoms balance trivially. The charge does not, and `Reaction.is_balanced` closes it by folding in
the metadata electron — which only works because step 1's propagation happened.

### Step 3 — RESOLVE ELECTRON PLACEMENT

The entry is removed from the registry first, to show the refusal, then restored — this is the
**shipped** declaration, not an injected one.

```
registry with the entry REMOVED : {'Plasma_Electron_Attachment': (1, 0),
                                   'Cation_R_Recombination': (1, 0)}
undeclared      : ElectronPlacementError: Family 'PlasmaElectronImpactIonization' has no
                  electron-placement declaration (reaction [Li] => [Lip], electrons=1);
                  refusing to infer electron placement from the net electron count...
registry (SHIPPED, no injection): {'Plasma_Electron_Attachment': (1, 0),
                                   'Cation_R_Recombination': (1, 0),
                                   'PlasmaElectronImpactIonization': (1, 2)}
rxn.family      : 'PlasmaElectronImpactIonization'
VIEW            : [Li] + e => [Lip] + e + e
view reactants  : ['[Li]', 'e']
view products   : ['[Lip]', 'e', 'e']
view.electrons  : 0 | view.reversible: False
view.comment    : Electron-placement view (family 'PlasmaElectronImpactIonization',
                  rate-order cross-check: agrees (order 2)) of: [Li] => [Lip]
E balance L/R   : 1 / 1
CANONICAL UNCHANGED: electrons=1 reactants=['[Li]'] products=['[Lip]']
```

Three things to read off it.

- **The refusal comes first.** Undeclared is a named failure, not a net-derived guess. That is the
  code-level half of §6.
- **A library label is a valid placement key.** `LibraryReaction.__init__` sets
  `self.family = library` **[R]** (`library.py:100`), so the registry — despite its name — accepts
  a library. This is what makes the library route possible at all; had it not, the code would have
  made the family-vs-library decision instead of the chemistry.
- **`(1, 2)` validates against the reaction's own electron count.** The declared net is
  `2 − 1 = +1`, which is `reaction.electrons`. The E pseudo-element balances at 1/1, which is the
  structural proof that the declared *sides* were the right sides, and the rate-order cross-check
  agrees at order 2 (view comment: `rate-order cross-check: agrees (order 2)`), which is the proof
  that the declared *incident order* matches the `cm³/(molecule·s)` coefficient. The canonical
  database reaction is byte-identical afterwards.

Four wrong declarations are refused, and it takes both guards to catch them **[M]** (parametrised
test): `(1, 3)` and `(1, 0)` fail the net-count check; `(0, 1)` and `(2, 3)` have the **right net**
and are caught only by the rate-order cross-check — `(0, 1)` is exactly the
factor-of-electron-density error that would otherwise ship silently.

### Step 4 — ACCEPTED BY THE PLASMA REACTOR

```
core species    : ['[Li]', '[Lip]', 'e']
ACCEPTED. reactor.electron_index = 2
kf (m^3/mol/s)  = [50315841.10550589]
k_Voronov(Te=10000 K) = 50315841.10550589
```

`PlasmaReactor.initialize_model` was handed the **canonical** reaction and resolved placement
itself, so this is the path a real model takes. Acceptance alone would not be enough — a view
evaluated at the wrong reaction order does not raise — so `kf` is compared against
`VoronovEIArrhenius.get_rate_coefficient_electron_temp(10000 K)` and matches exactly.

Rate behaviour across the fit's range, for context **[M]**:

| Tₑ | k (m³ mol⁻¹ s⁻¹) |
|---|---|
| 300 K | 6.87e−82 |
| 1 000 K | 4.41e−18 |
| 10 000 K | 5.03e+07 |
| 20 000 K | 1.63e+09 |

The 5.4 eV threshold is doing what it should: nothing at room temperature, a real channel at
plasma temperatures. Table validity is Tₑ = 1 eV … 20 keV (11 604.5 K … 2.3209e8 K) **[D]**.

### Negative control — attachment and cation recombination, unchanged

**[M]** Each of the two pre-existing shapes is resolved **twice**, once with the ionisation
declaration absent from the registry and once with it present, and the two views are compared
participant by participant:

| family | view | `electrons` | identical with and without the new declaration |
|---|---|---|---|
| `Plasma_Electron_Attachment` | `O2 + e => O2-` | 0 | yes |
| `Cation_R_Recombination` | `Lip + CH3 + e => CH3Li` | 0 | yes |

and `FAMILY_ELECTRON_PLACEMENT['Plasma_Electron_Attachment'] == (1, 0)`,
`['Cation_R_Recombination'] == (1, 0)` — both untouched. `Cation_R_Recombination` was **not
modified, copied, or used as a model**; it appears here only as a control, which is what the
ruling excluding it from plasma configurations permits.

---

## 6. What happens for a species the fits do not cover

**Nothing, and it is visible.** Named explicitly, because a silent fabricated rate fails this
ticket:

- **Data level.** A library has no template. An uncovered species is never offered an ionisation
  reaction — no match, no tree descent, no averaged rule, no estimate. Argon is *in* the Voronov
  table and RMG can build it, and it still gets nothing from this library, because coverage here
  is the entry list and nothing else.
- **Code level.** If someone adds a library or family for it without adding a placement
  declaration, `resolve_electron_placement` raises `ElectronPlacementError` by name, and
  `PlasmaReactor` independently refuses the metadata-only electron count. Both shown in §5 and
  both pinned by tests. There is no path from "undeclared" to "resolved with a guessed order".
- **The alternative is what makes this the answer.** A family would have converted the same
  absence into a *match followed by an averaged rule* — the failure mode that produced nine
  families that never match and one that matched and gave physically impossible rates.

The gap between 134 tabulated stages and 1 entry is therefore **not hidden generativity a family
would have unlocked**. It is 121 multiply-charged stages nothing here can represent, 5 elements
RMG has no atom types for, 1 cation atom type that does not exist, and 5 cations with no
thermochemistry. Every one of those blocks a family exactly as hard as it blocks a library.

---

## 7. The physical inverse of each forward channel — named, not implemented

**Forward channel entered here:** electron-impact ionisation,
`Li + e⁻ → Li⁺ + 2e⁻`, `VoronovEIArrhenius`, second order, Tₑ-driven.

**Its physical inverse is three-body (collisional) recombination:**

> `Li⁺ + 2e⁻ → Li + e⁻`

— third order, with the second electron carrying away the binding energy. That is the detailed
inverse of this channel: the same participants, run the other way. **[L]** It is the standard
partner of electron-impact ionisation in a collisional–radiative model, and its rate is
conventionally obtained from the ionisation coefficient through the Saha relation at Tₑ rather
than measured independently.

**Radiative recombination is a *different forward channel*, not this one's inverse:**

> `Li⁺ + e⁻ → Li + hν`

— second order, with a photon carrying the energy away. `input/kinetics/badnell.yaml` **[D]**
(Badnell, N. R. 2006, *ApJS* **167**, 334 **[L]**; 33 nuclear charges, 318 `(Z, N)` entries,
Li at `Z = 3, N = 2`) holds this fit, and it is deliberately **not entered** in this library. Its
own inverse is photoionisation `Li + hν → Li⁺ + e⁻`, which is a third distinct process.

**None of the three is implemented here.** The ticket forbids implementing a reverse rate, and the
representation makes that easy to honour rather than hard: because each channel is its own one-way
library entry, adding radiative recombination later is a new entry with its own `(1, 1)`
declaration and its own Badnell rate — it does not require, or permit, running this entry
backwards. If a future ticket wants collisional recombination it will need a third-order rate law
and a `(2, 1)` declaration, both of which the widened two-sided declaration already supports and
neither of which exists today.

---

## 8. What this ticket could not reach

Stated plainly, since a green suite is easy to over-read.

- **The placement declaration is committed, but on a different branch in a different
  repository.** `FAMILY_ELECTRON_PLACEMENT` lives in RMG-Py, so
  `'PlasmaElectronImpactIonization': (1, 2)` is `4a5bcba03` on RMG-Py branch
  `i114-ionisation-declaration`, **stacked on `i113-placement-widening`**. Two consequences worth
  naming: this library resolves only against a runtime carrying that branch, and if
  `i113-placement-widening` is rebased before it lands, the stacked branch needs
  `git rebase --onto`. Landing it also moved three registry tripwires I-113 had installed — each
  by hand, none loosened; see the RMG-Py commit message.
- **The database repository cannot verify the shipped declaration on its own.** The database test
  suite injects `(1, 2)` when the runtime does not carry it, so it is green against *both*
  runtimes. That is deliberate — it gets stronger, not weaker, once the RMG-Py branch merges — but
  it means a green database suite is not by itself evidence that the RMG-Py half exists.
- **No RMG model was run.** No `rmg.py` job, no enlargement, no convergence. `PlasmaReactor`
  accepted the reaction and evaluated it at the right rate; whether an ionisation channel survives
  flux filtering and pruning into a converged mechanism is a different question this did not ask.
  The same caveat `i041` §6 records applies unchanged.
- **Thermochemistry was stubbed for the reactor demonstration.** A constant-Cp NASA polynomial was
  used for Li, Li⁺ and e⁻. Nothing in the acceptance path depends on the values — the reaction is
  irreversible so no Keq is formed — but this is not a statement that the real thermochemistry
  works in a plasma reactor.
- **Only the neutral → +1 stage was considered at all.** The 121 ion → higher-ion stages in the
  table were not represented, tested, or costed.
- **Whether Li⁺ can then go anywhere.** `i041` established that no generation-time path in this
  database creates a cation, and that the `Cation_*` families need Li⁺ as an input species. This
  library is the first database entry that *produces* one. Whether the downstream cation chemistry
  is reachable from a Li⁺ this reaction made — rather than one a user supplied — was not measured
  here and is the natural next probe.
- **`average_kinetics`'s broken type guard** (§4.2) is reported, not fixed. It is an RMG-Py defect
  and would need its own ticket in that repository.
