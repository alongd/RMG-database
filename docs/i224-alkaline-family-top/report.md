# I-224 — Narrowing the top groups of `Plasma_Associative_Ionization_Alkaline_Alkaline`

Worktree `/home/alon/Code/RMG-database-i224-alkaline-family-top`, branch `i224-alkaline-family-top`.
Engine used for every measurement: `/home/alon/Code/RMG-Py-plasma` (branch `plasma`, tip `78f306665`),
via `PYTHONPATH`; RMG-Py was not modified.

**Revised after adversarial round 50**, which found nothing CRITICAL and nothing HIGH and
reproduced the narrowing, the gate clearance and the relocation independently against the same
engine. That round added one behavioural change — `allowChargedReactants = False`, with its own
section below — and five corrections to this document: the suite's structural blind spot is now a
finding of its own rather than a clause; the `A;B` node is described as holding two entries and
serving one; the training-index gap is marked documentary; the `alkaline` atom type is marked a
moving target; and "6 reactions / 0 unintended" now says which claim it is making.

## Resolved database directory

Every measurement pins and prints it as its first log line:

```
RESOLVED database.directory = /home/alon/Code/RMG-database-i224-alkaline-family-top/input
```

The baseline runs deliberately resolve elsewhere — a scratch tree whose only difference from the
worktree is a pristine copy of this one family:

```
RESOLVED database.directory = /tmp/claude-1000/.../scratchpad/basefull     (baseline)
```

Scripts set `settings['database.directory']` explicitly rather than relying on an `rmgrc`; the two
`pytest` runs, which cannot be told a path, run from scratch working directories carrying an
`rmgrc` that pins the tree under test. Logs: `docs/i224-alkaline-family-top/logs/`.

## Contradictions with the brief — measurements win

1. **The branch did not contain the family.** `i224-alkaline-family-top` was cut from `polymer`
   (`4a12d36fc`), where `input/kinetics/families/` holds no plasma family at all. The family lives
   on `plasma`. The branch had no commits of its own and no upstream, so it was reset to
   `plasma@d07add74a` — nothing lost, nothing pushed. Every number below is against that base.

2. **`rules.py` is empty, but `training/` is not.** The brief reports zero rate rules and stops
   there. `training/reactions.py` holds **three** reactions, one of them with a real literature
   rate:

   | entry | reaction | rate | rank | source |
   |---|---|---|---|---|
   | 1 | `O + O <=> O2+ + e-` | A=1.82e10 cm³/mol/s, n=0.6797, Ea=160336 cal/mol | 6 | [Aiken2025] Table VIII |
   | 2 | `Mg + Mg <=> Mg2+ + e-` | A=6.02e13, n=0, Ea=0 | 9 | estimated |
   | 3 | `Ca + Ca <=> Ca2+ + e-` | A=1.87e13, n=0, Ea=0 | 9 | estimated |

   This is the fact that decides the ticket, and it is why "no rate is selected today" understates
   the stake: training entries become rate rules on every real run.

3. **The tops were not authored here.** `git log --follow` shows one commit touching this file:
   `13d644248` (2026-08-29), the carry of three associative-ionisation families from branch 99. The
   wildcard tops arrived verbatim in that carry.

## What the family is for, from its own contents

`A + B <=> AB+ + e-`, where both partners are atoms carrying two unpaired electrons: one partner
(`*1`) gives up two radicals — one to the new bond, one to the departing electron — and takes the
`+1` charge; the other (`*2`) gives up one radical to the bond. The recipe says exactly that:

```
LOSE_RADICAL *1 2 ; LOSE_RADICAL *2 1 ; FORM_BOND *1 1 *2 ; GAIN_CHARGE *1 1
```

`electrons = 1`, `reversible = False`, with the reverse owned by a separate family
(`electron_absorbance_and_dissociation_3`). The docstring before this ticket read "both A and B
have two radicals, e.g.: alkaline earth metal atoms **or O atoms**", and the training set matches
that sentence: two alkaline-earth pairs and one oxygen pair. The tree carried the alkaline
restriction one level below the top, in `alkaline_A` / `alkaline_B`.

So the family is *named* for alkaline-earth associative ionisation, and was *built* to cover
alkaline-earth **and oxygen** associative ionisation. Those two statements are not the same, and
the whole ticket sits in the gap between them.

## Baseline

17-species representative set (the three training species; C, N, S, triplet CH2, triplet NH, a
carbene site inside C3H7, O2, Na, Li, H, ground-state Ar and He, Mg⁺, and OH⁺ as an `O u2` species
inside a polyatomic cation). Log: `logs/baseline.stdout.log`.

| quantity | baseline |
|---|---|
| species matching top `A` | 10 of 17 (3 intended, 7 unintended) |
| species matching top `B` | 10 of 17 (3 intended, 7 unintended) |
| reactions generated | **90** |
| — both partners intended | 12 |
| — at least one partner unintended | **78** |
| training reactions the family can generate | 3 of 3 |
| family checks passing (one at a time) | **12 of 12** |

The unintended matches are not exotic: C, N, S, CH2, NH, and a carbene carbon inside an arbitrary
polyatomic all match on every field, descend to the generic top, and generate a bonded cation.
`OH⁺` matches too and then *raises* `AtomTypeError` during generation (the recipe drives it to a
`c+2` oxygen), so the breadth was already producing logged errors, not merely junk reactions.

**Metastable argon could not be demonstrated either way.** `Ar u2 p3 c0` is not constructible on
this RMG-Py branch — the sibling ticket's atom type is not present — so the species that surfaced
this ticket cannot be tested here. That does not weaken the case: six other species already prove
the breadth.

## What landed

```
 entry A   1 *1 R u[2,3,4] px cx        ->   1 *1 alkaline u2 px cx
 entry B   1 *2 R u[2,3,4] px cx        ->   1 *2 alkaline u2 px cx
 alkaline_A  1 *1 alkaline u[2,3,4] px cx   ->  removed
 alkaline_B  1 *2 alkaline u[2,3,4] px cx   ->  removed
 tree      L1: A / L2: alkaline_A / L1: B / L2: alkaline_B  ->  L1: A / L1: B
```

`alkaline` is exactly `Mg` and `Ca` with their charge and spin variants
(`rmgpy/molecule/atomtype.py:388-389`), so the tops now name precisely the chemistry the family is
named for.

**Why the children went.** Under an `alkaline` top they cannot stay as they were: the pre-I-224
child is *broader* in radical count than the narrowed parent, which fails
`kinetics_check_child_parent_relationships`; and a child restated as `alkaline u2 px cx` would be
identical to its parent, which fails `kinetics_check_groups_nonidentical`. The restriction moved
up, so the node below it is redundant. Two bare roots is also the shape of the sibling family
`Plasma_Associative_Ionization_Alkali_Alkaline`, whose `B` top carries no children.

### Before and after, both directions

| quantity | baseline | landed | verdict |
|---|---|---|---|
| reactions generated | 90 | **6** | |
| — intended (both partners Mg/Ca/O) | 12 | **6** | **6 lost — every pair involving O** |
| — unintended | 78 | **0** | all removed |
| species matching top `A` | 10 (3 int, 7 unint) | 2 (2 int, 0 unint) | |
| species matching top `B` | 10 (3 int, 7 unint) | 2 (2 int, 0 unint) | |
| training reactions generatable | 3 of 3 | **2 of 2** | the third was moved out, see below |
| family checks passing, individually | 12 of 12 | **12 of 12** | no regression |
| `add_rules_from_training` | returns normally | **returns normally** | gate exercised, not assumed |

Retained: `Mg + Mg`, `Mg + Ca`, `Ca + Ca` (2 reactions each, the two charge assignments).
Dropped and intended: `O + O`, `O + Mg`, `O + Ca`. Dropped and unintended: every pair drawn from
C, N, S, CH2, NH, the polyatomic carbene, and OH⁺ — 78 reactions, to zero.

**What "6 reactions / 0 unintended" claims, and what it does not.** Six is raw generation
arithmetic: two matching species give three unordered pairs, and each pair is generated in both
slot orders (`*1` takes the charge, `*2` does not), so 3 × 2 = 6 is exactly the number a correct
template predicts. The claim being made is therefore **"the template does not over-generate"** —
nothing above the predicted count, and the 78 unintended are gone. It is **not** a claim that
coverage is complete, that six is the right number of alkaline-earth associative-ionization
channels in nature, or that these six reactions carry defensible rates. Coverage in fact went
*down*: three intended pairs involving oxygen were lost, which is the subject of the next section.
Whether the retained chemistry is right is untouched — see "What this could not reach".

**`alkaline` is a moving target, and the top now says so.** The narrowing means "whatever the
`alkaline` atom type resolves to", which is Mg and Ca today (`atomtype.py:388-389`). If Be, Sr or Ba
are ever added to that atom type, these tops widen to admit them with no edit to `groups.py` and no
check failing, while the training set stays Mg and Ca only — a widening of the atom type would
outrun the data before it outran the family's name. A sentence recording this is now in the
`groups.py` docstring, which is where someone editing the atom type would have a chance of seeing
it.

## The orphaned training reaction — measured, then moved

This ticket went through two states, and both are reported because the intermediate one carries the
finding.

**State 2 — narrowed, entry left in place.** The O + O entry was kept where it was, with the
orphaning recorded in `training/reactions.py` and in the `groups.py` docstring.

**State 3 — entry moved out (what is committed).** The entry now lives at
`docs/i224-alkaline-family-top/held-back/Plasma_Associative_Ionization_Alkaline_Alkaline/training/`,
the layout `docs/i154-carry-chemistry/held-back/` already uses for chemistry the campaign is not
ready to install. It is **not deleted and not installed**: `docs/`, never `input/`. `diff` against
the pre-I-224 original shows the entry identical in index, label, degeneracy, kinetics, rank and
reference, differing only by an added provenance note in its `longDesc`; the three species
definitions (`O_A`, `O_B`, `O2p`) moved with it and are byte-identical. The surviving entries keep
indices **2 and 3** — index 1 is deliberately absent from the family, so the two files match up by
number.

**That index gap is a documentary signal, not a durable fact.** `Database.save(path, reindex=True)`
is the default (`rmgpy/data/base.py:362-372`), and `get_entries_to_save` ends with
`for index, entry in enumerate(entries): entry.index = index` (`base.py:295-296`). So the moment
anything saves this depository through RMG's own writer, the surviving entries become 0 and 1 and
the gap closes silently. The gap survives only as long as the file is edited by hand, which is how
it is maintained today. Anyone who needs the link to be durable should rely on the prose note in
`training/reactions.py` and on the held-back copy's own provenance block, not on the numbering.

The held-back copy records what it is, that it left because the narrowing put oxygen
outside the template rather than because it was judged wrong, that it wants a family named for
neutral associative ionization, and that the prerequisite for such a family is an RMG-Py change
this ticket does not make.

What the orphan does, measured one call at a time (`logs/addrules-*.stdout.log`):

| call | 1. baseline | 2. narrowed, entry in place | 3. entry moved out |
|---|---|---|---|
| training entries in the family | 3 | 3 | 2 |
| `get_reaction_template_labels(O + O)` | `['A', 'B']` | **raises `UndeterminableKineticsError`** | n/a — entry is held back |
| `get_reaction_template_labels(Mg + Mg)` | `['alkaline_A', 'alkaline_B']` | `['A', 'B']` | `['A', 'B']` |
| `get_reaction_template_labels(Ca + Ca)` | `['alkaline_A', 'alkaline_B']` | `['A', 'B']` | `['A', 'B']` |
| `add_rules_from_training(thermo_database=<real>)` | returns normally | **raises `UndeterminableKineticsError`** | **returns normally** |
| rate-rule nodes produced | 2 (`A;B` rank 6, `alkaline_A;alkaline_B` rank 9 ×2) | 1 (`A;B` rank 9 ×2), then the raise | 1 (`A;B` rank 9 ×2), no raise |
| all 12 family checks, one at a time | PASS | **PASS** | PASS |
| wider suite | 6 passed | 6 passed | 6 passed |

**This is the result you asked to see, and it is worse than a red check.** No check goes red. The
family is green through every method in `databaseTest.py`, invoked individually, and it still takes
a real run down: `rmgpy/rmg/main.py:590` calls `add_rules_from_training` for every non-auto-generated
family, and the unmatched entry escapes it. The suite does not miss this by bad luck; it cannot see
it at all, for a structural reason that is the next section.

Mechanism: `add_rules_from_training` catches `UndeterminableKineticsError` for the forward direction
and files the entry under `reverse_entries` (`family.py:1184-1191`), then re-tries it in reverse; the
reverse (`[O][O+] -> ...`) does not match the template either, and that second failure is not caught.

**An earlier number in my own measurement was wrong and is corrected here.** My first probe passed
`thermo_database=None` and reported `AttributeError: 'NoneType' has no attribute 'get_thermo_data'`.
That was the probe's defect, not the family's — the reverse-entry path needs a real thermo database.
Re-run with one, the failure is the `UndeterminableKineticsError` above.

**State 2 was green-and-broken-at-run-time — a merge gate, not a footnote.** State 3 clears it, and
the clearance was exercised rather than assumed: `add_rules_from_training`, called with a real
thermo database exactly as `main.py:590` calls it, **returns normally** and produces the one
expected rule node `A;B`, carrying the two rank-9 alkaline-earth **entries** — of which it serves
one; see "The `A;B` node holds two entries and serves one" below. Nothing was left on stderr.
So the orphan was the only trigger of the uncaught reverse-miss path for this family; had it not
cleared, that would have meant a second trigger at `family.py:1184-1191`, and the instruction was
to stop and report rather than chase it.

**What remains open is chemistry, not a defect.** O + O associative ionization is still real,
sourced, rank-6 chemistry with nowhere to live. It is preserved verbatim under `docs/`, and it
needs a family named for neutral associative ionization — which needs the oxygen atom types to gain
a charge row in RMG-Py first. Neither is built here.

## Finding: the database suite never exercises `add_rules_from_training` for a gas-phase family

This is the strongest thing the ticket produced, and the first version of this report left it as a
clause inside the paragraph above. It is not a check that happened to be looking the wrong way.

`test/database/databaseTest.py` calls `add_rules_from_training` in exactly **one** place, inside
`kinetics_check_surface_training_reactions_can_be_used` (`databaseTest.py:365-370`, the call itself
at `:369`):

```python
    def kinetics_check_surface_training_reactions_can_be_used(self, family_name):
        """Test that surface training reactions can be averaged and used for generating rate rules"""
        family = self.database.kinetics.families[family_name]
        if not family.auto_generated:
            family.add_rules_from_training(thermo_database=self.database.thermo)
            family.fill_rules_by_averaging_up(verbose=True)
        return True
```

and `test_kinetics` invokes that check only from inside a name gate (`databaseTest.py:130`):

```python
            # tests for surface families
            if "surface" in family_name.lower():
```

**General form.** *No check in the database suite exercises `add_rules_from_training` for a
gas-phase family, so the class of defect this ticket found is invisible to the suite by
construction, not by accident.* Every gas-phase family in the database — including every plasma
family this campaign carries — is never run against the function that crashes. A training entry the
recipe cannot reach passes the entire suite on any non-surface family, every time, forever. The
measurement that makes this concrete is in the table above: at state 2, twelve of twelve family
checks and `6 passed` on the whole suite, alongside `add_rules_from_training` raising
`UndeterminableKineticsError` on the path `rmgpy/rmg/main.py:590` takes.

**What would close it, and who owns that.** The smallest honest answer is that the check has no
reason to be surface-gated: `add_rules_from_training` and `fill_rules_by_averaging_up` are not
surface-specific, the method's own body is already guarded by `if not family.auto_generated`, and
running it for every family is what `main.py` does anyway. Renaming it and lifting it out of the
`"surface"` branch would turn a class of run-time crash into a test failure. **This is a referral,
not a change**: `databaseTest.py` lives in RMG-Py, which this ticket does not touch. Two families
are already known to reach that call and fail for unrelated reasons — this one via an unreachable
training entry, and `Plasma_Electron_Impact_Dissociation` via `TwoTemperaturePlasma` kinetics — which
is enough to suspect a pattern rather than two accidents, and enough to justify the referral.

**What the referral does not cover.** Lifting the gate would exercise the call for ~100 gas-phase
families that have never been run through it in CI; how many of them would go red is not measured
here, and finding out is the sweep, not this ticket.

## Finding: the wildcard top may be a workaround for an incomplete atom-type action table

Verified, not assumed (`logs/gaincharge-vocabulary.stdout.log`):

- `ATOMTYPES['O']` has `increment_charge=[]` **and** `decrement_charge=[]`, while its bond, radical
  and lone-pair actions are all self-preserving (`increment_bond=['O']`, `increment_radical=['O']`,
  `increment_lone_pair=['O']`, …). The charge row alone is missing.
- `Mg`, `Ca` and `alkaline` are fully self-preserving **including** charge
  (`atomtype.py:841, 851, 857`).
- Of 164 atom types, only 36 carry an `increment_charge` action, and the only oxygen-bearing one is
  `Om2`, the −2 oxide.
- `GroupAtom._gain_charge` (`group.py:362-385`) raises `ActionError` unless **every** atom type in
  the group's union has one. Measured directly: a top of `[Mg,Ca,O] u2 px c0` on `*1` aborts family
  loading with `ActionError: Unknown atom type produced from set "[Ca, Mg, O]"`.

The recipe applies `GAIN_CHARGE` to `*1`, and the family's own training set needs oxygen **in the
`*1` slot** (the training dictionary's `O2p` puts the `c+1` on `*1`). Those two facts together mean
**no `*1` top that names oxygen can load at all.** If the author wanted the O + O entry to work,
a wildcard on `*1` was not a lazy choice — it was the only choice the engine allowed. That reframes
the defect: a database paying for an engine gap, not sloppy authoring.

The framing is exact for `*1` and does **not** extend to `*2`. `*2` never gains charge, and
`[Mg,Ca,O] u2 px cx` loads and matches correctly there — measured. So the `*2` wildcard is not
explained by the engine gap; mirroring `*1` is the likeliest reason, but that is inference, not
measurement.

## Finding, generalised: a training reaction whose rate lands on a root node

Kept here because it outlives the oxygen instance that prompted it.

Measured at baseline: `add_rules_from_training` put the O + O rate — **rank 6, Ea = 670846 J/mol
(160 kcal/mol)** — on the rule node `A;B`, the *root*. The Mg and Ca rates landed one level down on
`alkaline_A;alkaline_B`. A root rule is the fallback for everything that descends no further, so at
baseline any Mg/Ca pair without its own rule would have inherited a 160 kcal/mol barrier measured
for oxygen. The general statement:

> A family must never carry a training reaction its tree cannot reach at the right granularity.
> Too coarse, and the rate becomes the fallback estimate for unrelated chemistry; unreachable, and
> the entry is silently dead — and neither condition is visible to `test_kinetics`.

The narrowing incidentally removes the first half of that hazard: after it, the root `A;B` carries
the Mg and Ca rates, which is the right granularity for a tree whose root *is* the alkaline node.
It replaces it with the second half, for oxygen.

## The `A;B` node holds two entries and serves one

An earlier draft of this report read as though the surviving rule node carries two rates. It carries
two **entries** and serves **one**. Measured (`logs/ruleselection.stdout.log`), after
`add_rules_from_training` on the committed tree:

```
get_all_rules(A;B) -> 2 entries AT THE SAME NODE
  index=1 rank=9  A=3.01e+13 cm^3/(mol*s)   "From training reaction 2 used for A;B"   (Mg)
  index=2 rank=9  A=9.35e+12 cm^3/(mol*s)   "From training reaction 3 used for A;B"   (Ca)

get_rule(A;B) SERVES exactly one: index=1  A=3.01e+13
  NEVER-SERVED index=2  A=9.35e+12
```

**Mechanism.** `estimate_kinetics` asks `KineticsRules.get_rule(template)`, which collects every
entry filed under the template label and, when there is more than one, sorts them on
`(rank, index)` and returns `entries[0]` (`rmgpy/data/kinetics/rules.py:141-156`; rank 0 or `None`
is given an effective rank of 1000). Both entries are rank 9, so the tie falls to the index, and the
lower index wins. `fill_rules_by_averaging_up` does not intervene: it fills *gaps* in the tree, and
`A;B` is not a gap. (The rule A-factors are half the training A-factors — 6.02e13 and 1.87e13 — because
both training entries carry degeneracy 2.)

**Consequence, stated plainly: this family cannot distinguish Mg from Ca at the template level.**
Any Mg/Ca pair that reaches this family is estimated from the Mg training reaction; the Ca rate is
carried in the depository, converted into a rule, and then never returned. Distinguishing them needs
a tree level below the tops — exactly the level the narrowing removed, and removing it was the point
of the ticket, since under an `alkaline` top a re-stated `alkaline` child fails
`kinetics_check_groups_nonidentical`. Separate `Mg`/`Ca` nodes would be a different shape from the
one this ticket was asked for, and are not built here.

**This is pre-existing, not a regression.** Before the narrowing both entries sat together on
`alkaline_A;alkaline_B` and the same one won by the same rule; what changed is that the collision
now sits on the root node and there is no longer a level above it. Nothing is broken — but it is a
real limitation of the result and should not be discovered by whoever reads this next.

## Finding: `allowChargedReactants = False` — declared, and measured to change nothing today

`groups.py` declares `allowChargedSpecies = True`, which is **two-sided**: it gates reactants and
products together (`family.py:688-695`). The charged product is the entire point of this family, so
that flag has to stay True, and before this round `allowChargedReactants` was undeclared and
therefore inherited it — the reactant side was charge-open while the family's own docstring said it
associates two neutral atoms. The groups cannot say it either: RMG groups match subgraphs, so a
`c0` on `*1` constrains that atom and never the molecule around it, and the tops' `cx` constrains
nothing at all. `allowChargedReactants` is mainline's one-sided reactant override for exactly this
case (`family.py:576-580`, `:693-695`, `is_charged_reactant_forbidden` at `:1726-1740`, applied to
the forward reactants in `_create_reaction` at `:1788-1792`). It is now declared `False`. One other
family in this database already does the same: `Plasma_Electron_Attachment/groups.py`.

**Measured effect: none today, in generation.** Logs `logs/chargedreactants-before.*` (the tree at
`e56fd307e`, family copied into a scratch tree so the two runs differ only in this declaration) and
`logs/chargedreactants-after.*`:

| quantity | before (inherits `True`) | after (`False`) |
|---|---|---|
| `family.allow_charged_species` | True | True |
| `family.allow_charged_reactants` | **True** (inherited) | **False** (declared) |
| reactions over the 17-species set | 6 | **6** |
| reactions over the charged-spectator set | 6 | **6** |
| `is_charged_reactant_forbidden(Mg··H⁺)`, net +1 | False | **True** |
| `is_charged_reactant_forbidden(Ca··H⁺)`, net +1 | False | **True** |
| `is_charged_reactant_forbidden(Mg··O⁻)`, net −1 | False | **True** |
| `is_charged_reactant_forbidden(Mg··H⁺··H⁺)`, net +2 | False | **True** |
| `is_charged_reactant_forbidden(Mg··H⁺··O⁻)`, net **0** | False | False |
| `is_charged_reactant_forbidden(Mg)`, net 0 | False | False |
| 12 family checks, one at a time | 12/12 | **12/12** |
| `add_rules_from_training` | returns normally | **returns normally** |

The declaration is read and it does arm the predicate — four species flip from admitted to forbidden
— but **no reaction count moves**, because nothing that the predicate now refuses was reaching the
recipe anyway. Two independent layers were already stopping it, and both are worth recording because
they bound what the declaration is protecting:

1. **A charged alkaline-earth atom at `u2` cannot exist.** Exhaustively, over `Mg` and `Ca` × charge
   −1…+2 × 0…2 bonds (`logs/chargedreactants-after.stdout.log`, section B0), the **only**
   constructible combination is neutral with zero bonds; every other is refused by RMG's valency
   model with `InvalidAdjacencyListError` (or `AtomTypeError` at `c-1` with one bond). So although
   `ATOMTYPES['alkaline']` does contain `Mg+, Mg+2, Ca+, Ca+2` and the tops' `cx` admits them at the
   group level, no molecule can present one to these tops. Any *connected* molecule matching these
   tops **is** a bare neutral atom.
2. **A charge on a disconnected spectator fragment is refused one layer earlier than the charge
   policy.** A species like `Mg··H⁺` (net +1) does match both tops — `_match_reactant_to_template`
   returns one mapping against each — but generation still yields nothing, and the reason is not
   charge: the merged structure splits into two products against a template declaring one
   (`template(products=["AB+"])`), so `apply_recipe` returns `None` at `family.py:1525-1532`, before
   `_create_reaction` is ever called. Traced on **both** trees, with `_create_reaction`,
   `_generate_product_structures` and `apply_recipe` instrumented:
   `logs/vdw-productcount-probe-before.stdout.log` shows `apply_recipe -> None` while
   `is_charged_reactant_forbidden` is still `False` — so the refusal is not the charge policy's —
   and `logs/vdw-productcount-probe-after.stdout.log` shows the same `apply_recipe -> None` with the
   predicate now `True`, i.e. the declaration never gets the chance to be the reason.

**So why keep it?** Because both of those are accidents of the current shape, not statements of
scope. Widen the radical count, write a bonded group, or declare a second product, and the reactant
side is charge-open again with no edit to this file and no check failing — the same
silently-widening hazard as the `alkaline` atom type itself. The declaration costs one net-charge
test per candidate reactant and converts a property the family currently has by luck into one it
states. It is a family-local restriction on this family's declared scope, not a claim that
associative ionization of an ion is impossible chemistry.

**Read the criterion literally.** It is *net* charge: the charge-separated but net-neutral
`Mg··H⁺··O⁻` is **not** refused, before or after — correctly, since the predicate draws its line at
net charge and nowhere else.

## Findings that cost time and should not be re-learned

1. **A generic atom type unioned with an element silently loses the generic's members.**
   `[alkaline,O] u2 px cx` matches O but **not** Mg or Ca. `Group.get_element_count`
   (`group.py:2013-2043`) scans the union left to right, skips `alkaline` (no element matches), then
   lets `O` set `elementCount = {'O': 1}`; `Molecule.is_subgraph_isomorphic`
   (`molecule.py:1780-1786`) then rejects every oxygen-free molecule **before** any atom-type
   comparison. The order-swapped `[O,alkaline]` works — by accident of the same scan. `[Mg,Ca,O]`
   works correctly. Nothing warns.

2. **A pinned `c0` on a wildcard top fails `kinetics_check_sample_descends_to_group`.**
   `make_sample_molecule()` on `R u2 px c0` fabricates `H u2 p0 c-1` — charge −1 — which then fails
   to match the group it came from. With `cx` the same fabricated sample matches, so the check
   passes for the wrong reason. `R!H u2 px c0` fabricates neutral CH2 and passes.

3. **A stray subdirectory inside a family directory breaks database loading.** An empty
   `.claude/.cc-writes/` created by the editing harness inside the family directory made
   `RMGDatabase.load(..., kinetics_depositories='all')` die with
   `FileNotFoundError: .../Plasma_Associative_Ionization_Alkaline_Alkaline/.claude/reactions.py`.
   Git never reported it, because git does not track empty directories. Removed; worth a glance
   before blaming a family for a load failure.

4. **`R!H` is not a metal-free wildcard.** Its `specific` list contains `Ar, Ar0, Ar0s, Ar+, Ar++`
   (`atomtype.py:325-327`), so a top of `R!H u2 px c0` would still match metastable argon once that
   atom type lands — it narrows the *state*, not the *element*. This is what disqualified the
   partial narrowing I had first measured and recommended.

## Rejected alternative, with its numbers

For the record, since it was measured before it was rejected: `*1 = R!H u2 px c0`,
`*2 = [Mg,Ca,O] u2 px c0`, children `[Mg,Ca] u2 px c0` gave 90 → 24 reactions, kept all 12 intended
reactions and all 3 training reactions, left 12 unintended, and passed 12 of 12 checks. It was
rejected because `R!H` still admits argon and every other non-metal with a `u2` atom: it narrows the
radical state, not the element, and the element is what the family name constrains.

## Wider database suite

`pytest test/database/databaseTest.py`, run from a working directory whose `rmgrc` pins the tree
under test, once per tree, in separate processes.

| tree | collected | passed | failed | wall |
|---|---|---|---|---|
| 1. baseline (pristine family) | 6 | **6** | 0 | 511.88 s |
| 2. narrowed, entry in place | 6 | **6** | 0 | 493.58 s |
| 3. entry moved out | 6 | **6** | 0 | 468.19 s |
| 4. `allowChargedReactants = False` (committed) | 6 | **6** | 0 | 465.84 s |

Same six tests in all four, same outcome each: `test_kinetics`, `test_thermo`, `test_transport`,
`test_solvation`, `test_statmech`, `test_metal_libraries`. No new failure, and no test that passed
at baseline stopped passing. Note what that does *not* mean: on tree 2, `test_kinetics` is green
while `add_rules_from_training` raises, for the structural reason given above — which is exactly
why the gate had to be exercised separately rather than inferred from a green suite. Logs:
`logs/suite-baseline.*`, `logs/suite-after.*`, `logs/suite-orphan-removed.*`, `logs/suite-rework.*`.

## What this could not reach

- **Metastable argon.** `Ar u2 p3 c0` is not constructible on this RMG-Py branch, so the species
  that opened the ticket was never tested against either the old or the new top. The case against
  the old top rests on six other species; the case that `R!H` would not have excluded argon rests on
  `R!H`'s `specific` list, not on a match test.
- **Rate selection inside a production run.** `rules.py` is still empty by design, so every rule
  this family has exists only in memory, built from `training/` by `add_rules_from_training`. The
  `(rank, index)` tie-break is measured on those in-memory rules (`logs/ruleselection.stdout.log`),
  but no RMG job was run, so nothing here shows what `estimate_kinetics` returns to a live model,
  and the root-node hazard's consequences for estimated rates stay unproven until someone populates
  that file or runs a job.
- **How much the surface-gate referral would uncover.** Lifting the `"surface"` gate would exercise
  `add_rules_from_training` for every gas-phase family in the database. How many of those would then
  fail is not measured here — two are known (this one before the move, and
  `Plasma_Electron_Impact_Dissociation`), and establishing the rest is a separate sweep.
- **What `allowChargedReactants = False` protects against.** It is measured to change no reaction
  count today, and the two reasons why are measured (valency, and the product-count guard). What is
  *not* measured is the future case it exists for: no widened top, bonded group or second declared
  product was constructed to watch the declaration actually refuse a reaction. The evidence that it
  arms is the predicate flipping on five species, not a suppressed reaction.
- **Whether the retained chemistry is right.** This ticket measured *reachability*, not chemistry.
  The Mg and Ca rates are rank 9, "estimated", with no source; nothing here checks whether
  `Mg + Mg <=> Mg2+ + e-` is a real channel at the conditions this campaign runs, or whether
  `A=6.02e13, Ea=0` is defensible.
- **Reaction generation inside a real run.** All generation here is direct
  `family.generate_reactions` calls on hand-built molecules. No RMG job was run; the
  `add_rules_from_training` failure is measured by calling that method exactly as `main.py:590`
  does, not by running a job to its crash.
- **The reverse family.** `electron_absorbance_and_dissociation_3` was not loaded or examined. If
  its tops mirror the pre-I-224 wildcards, it has the same defect, untouched — the ticket forbids
  other families.
- **The sibling families' own tops.** `Plasma_Associative_Ionization_Alkali_Alkali` uses
  `alkali u1 px cx` for `*2`, which is a single generic and therefore matches correctly; it was read
  but not measured, and not touched.
- **The held-back copy is a fragment, not a family.** It carries a training depository only — no
  `groups.py`, no `rules.py` — because the family it belongs to does not exist yet. It was never
  loaded by RMG, so nothing here proves it parses as a depository in its new location; what is
  verified is that it is byte-identical to what left, by `diff`.
- **The destination family.** Not designed, not named, not stubbed. Whether neutral associative
  ionization is best served by one family or several, and what its `*2` side should admit, is
  untouched work.
- **That a real RMG run now starts.** The cleared gate is measured at the level of the call
  `main.py:590` makes, with a real thermo database. No RMG job was launched, so nothing here proves
  the wider deck runs — only that this family no longer raises at that call.
