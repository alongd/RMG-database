# D-008 — `Aryl_Decarbonylation` template diagnosis: the stated cause is REFUTED

**Branch:** `i014-decarbonylation` (local only; not merged, not pushed)
**Worktree:** `/home/alon/Code/RMG-database-i014-decarbonylation`
**Date:** 2026-08-01; A-factor correction added 2026-08-03
**Subject:** why the r117 carbon-phenolic run (`/home/alon/runs/CKMG/101/r117_edge500k/`,
125,360 edge species) produced zero CO.

---

## Verdict, stated first

**The diagnosis handed to this dispatch is wrong, and no change to the template is warranted.**

*(A separate defect — a misattributed A factor in this family's training entry — was found in
passing and corrected on 2026-08-03 under Alon's ruling. It has nothing to do with why r117
made no CO; see "RESOLVED" below.)*

The r117 terminal report (`TERMINAL_REPORT.md` §2, §5, §6) states:

> its template requires a carbonyl **on an aromatic ring**. Every carbonyl the model actually
> generates is on a **non-aromatic** ring […] so the template's group tree cannot match it.

Both halves of that sentence fail:

1. The template does **not** require an aromatic ring. It requires a **non-aromatic** one —
   the localized keto form. The claim is inverted.
2. The family **does** fire, in this database, on the run's own core radicals — including
   species `3606`, the exact dimethylphenoxy radical the report identifies as the dominant
   core species.

Per the dispatch's own instruction ("If the diagnosis is wrong, say so and stop"), no template
was widened and no new family was written. What was added is a regression test that pins the
template's real matching boundary so this misdiagnosis cannot recur.

---

## Q1 — Does the template require aromaticity at the carbonyl centre? No. It requires the opposite.

`input/kinetics/families/Aryl_Decarbonylation/groups.py`, the sole `Root` entry — this is the
**entire** template; the tree is one level (`L1: Root`):

```
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3 *3 C   u1 {1,S} {5,S}
4 *4 Cd  u0 {1,S} {7,D}
5    Cd  u0 {3,S} {6,D}
6    Cd  u0 {5,D} {7,S}
7    Cd  u0 {6,S} {4,D}
```

Not one atom is aromatic. Ring atoms 4–7 are `Cd` — *non-aromatic* double-bonded carbon. In
RMG's atomtype tree `Cd` and `Cb` are **siblings**, both children of `C`; `Cb` is not a
descendant of `Cd`. Verified directly (`testing/test_aryl_decarbonylation.py::test_template_is_not_aromatic`):

```
Cd.specific = ['Cd', 'Cdc']          -> 'Cb' NOT in Cd.specific
C.specific  = [..., 'Cb', 'Cbf', ...] -> 'Cb' IS in C.specific
```

So a genuinely aromatic ring **cannot** match atoms 4–7. The template is written on the
dearomatized cyclohexadienone ring, which is exactly the motif the report says it excludes.

The family's own `longDesc` says so in as many words, and had it been read the whole
investigation would have gone differently:

> The template is written on the LOCALIZED keto (cyclohexadienon-2-yl) resonance form, **not
> the aromatic Ar-O. form** […] so the family fires through them in ordinary reaction
> generation without any aromatic-bond machinery.

**What actually gates the match** is atom `*3`: `C u1` — an unpaired electron alpha to the
ring carbonyl. The family consumes a cyclohexadienon-2-**yl radical** (the keto resonance
form of an aryloxy radical), not a closed-shell cyclohexadienone. The species the dispatch
cites — `CC1=CC=CC(=O)C1Cc1ccc(C)cc1O`, and r117's `125407` / `125409` — are closed-shell at
the relevant centre, or carry their radical too far from the carbonyl. They fail on the
**radical** requirement, not on aromaticity. That refusal is chemically correct (see Q4).

The template has **never** been anything else: `git log` shows `groups.py` has exactly one
commit, `e573fc979` (2026-07-22 18:43), never amended. The family entered the `polymers` set
in `2a932fc77` (2026-07-22 19:25), a week before r117 launched. The r117 run saw a
byte-identical template to the one tested here.

## Q2 — Is there an existing family that covers the chemistry? Yes — this one.

There is no gap to fill. `Aryl_Decarbonylation` already covers the real CO channel of phenolic
pyrolysis (aryloxy radical → cyclopentadienyl + CO), and it demonstrably fires on the r117
model's own species. Live output, this database:

| substrate | SMILES | reactions | products |
|---|---|---|---|
| phenoxy (training anchor) | `[O]c1ccccc1` | 2 | `[C-]#[O+]` + `[CH]1C=CC=C1` |
| p-cresoxy (r117 deck seed) | `[O]c1ccc(C)cc1` | 2 | `[C-]#[O+]` + `CC1=C[CH]C=C1` |
| m-cresoxy (r117 deck seed) | `[O]c1cccc(C)c1` | 2 | `[C-]#[O+]` + `CC1=CC=C[CH]1` |
| **dimethylphenoxy — r117 species 3606** | `Cc1ccc(C)c([O])c1` | **2** | `[C-]#[O+]` + `C[C]1C=CC(C)=C1` |
| novolac dimer aryloxy | `[O]c1ccc(C)cc1Cc1ccc(C)cc1O` | 2 | `[C-]#[O+]` + `CC1=C[C](Cc2ccc(C)cc2O)C=C1` |
| hydroxyphenoxy | `[O]c1ccccc1O` | 2 | `[C-]#[O+]` + `O[C]1C=CC=C1` |

Both r117 deck seeds (`p_cresoxy`, `m_cresoxy`) are *input species*, hence core species from
iteration 0, and the family matches both.

The family also works **end to end**, not merely at the template layer. Replicating RMG's own
rate-rules path (`rmgpy/rmg/main.py:484-494`: `add_rules_from_training` then
`fill_rules_by_averaging_up`) populates the single `Root` rule from the Lin & Lin training
anchor and resolves kinetics for every substrate at Euclidean distance 0 (exact `Root` match):

```
RULE[Root] ArrheniusEP(A=(1.255e+11,'s^-1'), n=0, alpha=0, E0=(183678,'J/mol'),
                       Tmin=(1000,'K'), Tmax=(1580,'K'))
[O]c1ccccc1      -> [C-]#[O+] + [CH]1C=CC=C1      | k = <above>
Cc1ccc(C)c([O])c1 -> [C-]#[O+] + C[C]1C=CC(C)=C1  | k = <above>   (r117 species 3606)
[O]c1ccc(C)cc1   -> [C-]#[O+] + CC1=C[CH]C=C1     | k = <above>   (r117 deck seed)
```

`A = 1.255e11 s⁻¹` is the training value `2.51e11` divided by the declared degeneracy of 2, and
`E0 = 183678 J/mol = 43.9 kcal/mol`, exactly as the training entry specifies. So template
match, recipe, product constraints, and kinetics assignment all succeed.

*(These A values are post-correction. When this section was first written on 2026-08-01 the rule
read `A = 3.7e+11 s⁻¹`, from the then-coded training value of `7.4e11`. The A factor was
corrected on 2026-08-03 — see "RESOLVED" below. Nothing else in this section changed: the
correction moved a number, not the matching behaviour.)*

The products also clear r117's own `generatedSpeciesConstraints` verbatim
(`maximumCarbonAtoms=15, maximumOxygenAtoms=2, maximumHeavyAtoms=17, maximumRadicalElectrons=2,`
`maximumSingletCarbenes=1, maximumCarbeneRadicals=0`): CO as the singlet carbene `[C]=O`,
CO as `[C-]#[O+]`, and methylcyclopentadienyl all return `ACCEPTED` from
`rmgpy.constraints.fails_species_constraints`. The `maximumSingletCarbenes=1` workaround that
`docs/kinetics_development_status.md` records as necessary for the CO product **is** set in
r117's deck, so that known RMG-Py veto was not in play either.

## Q3 — What is the minimal correct change? None to this database.

The cheapest fix was option zero — a family that is already there and simply is not being
reached — and that is what the evidence supports. Adding training reactions, widening the
template, or writing a new family would each be a change made to fix a defect that does not
exist, and a widened template would carry real over-matching risk (Q4) for no gain.

**Where the r117 evidence is actually weak.** The report's three nulls (§3) were all measured
against `chem_annotated.inp`. That file contains the **core** mechanism only, and r117 ran with
`saveEdgeSpecies=False`, so no edge Chemkin file was ever written. The 125,360-species edge was
therefore never inspected. What the greps establish is *"no CO-forming reaction reached the
core"* — not *"the family never fired."* Those are different claims, and the report's §2/§5/§6
assert the second on evidence for the first.

Given that the family matches both `p_cresoxy` and `m_cresoxy` — core species from iteration 0 —
the decarbonylation reactions were most likely generated into the edge on the first enlargement
and simply never promoted, since both seeds sit at mole fraction `1e-12` and the model's flux
went entirely into bimolecular condensation. That is a **flux/promotion** condition, not a
template condition. It is a hypothesis, not a finding: closing it requires `RMG.log` (31 MB,
on zeus, not retrievable within this dispatch's limits).

## Q4 — The real chemistry, and why a one-step closed-shell family would be a fiction

*Literature detail is carried in the "Chemistry and literature" section below.*

Two distinct substrates must not be conflated:

**(a) Aryloxy radical → cyclopentadienyl + CO.** Real, dominant, and already implemented. It is
*not* elementary — it is three elementary steps (details below), the rate-limiting one being
ring-opening of a bicyclic intermediate. The family books the **net** channel with measured
effective Arrhenius parameters, which is the standard mechanism-level treatment and is
explicitly declared in the family's `longDesc` and in its training entry. That is an honest
lumping: the net step is what was measured, and the intermediates are not kinetically
significant at pyrolysis temperatures.

**(b) Closed-shell cyclohexa-2,4-dien-1-one → CO.** This is the step the dispatch's premise
would have required, and it should **not** be added. A closed-shell dienone at 1000–1400 K does
not extrude CO in one step; its accessible fates are re-aromatization (tautomerization back to
the phenol), retro-Diels–Alder, or — for the 6,6-disubstituted adducts r117 actually makes —
homolysis of the weak sp3 C–C bond back to the two aryloxy radicals that formed it. A one-step
closed-shell CO-loss family would be precisely the convenient fiction the dispatch warns
against: right product, wrong reason, and it would over-fire on every saturated and aromatic
ketone in the model.

**The productive redirect** is (b) → (a): the dienone adducts are not a CO source, they are a
*sink that should be reversible*. The literature is emphatic here — the C–C bond joining two
coupled phenoxy radicals is extraordinarily weak (6.1 ± 0.5 kcal/mol for a crystallographically
characterized para-coupled keto dimer with **zero** bond dissociation free energy; ~14–20
kcal/mol for less-hindered trialkylphenoxyl keto dimers), so at 1000–1400 K these adducts
redissociate ~10 orders of magnitude faster than they do anything else. They are a fast
pre-equilibrium reservoir, not a product. If the model lets them redissociate, the aryloxy
radicals come back and the CO channel that already exists takes over.

At the family layer this is not blocked: `R_Recombination`, `Ketoenol` (in `default`) and
`Ketoenol_Aromatic` (in `polymers`) all engage these adducts when probed directly. Whether the
reverse actually carries flux in a run — and whether RMG's thermochemistry reproduces a C–C
bond this weak, which is the real risk, since a group-additivity estimate will not know about
the double resonance stabilization — is the live question this dispatch did not close.

---

## Chemistry and literature

### (a) Phenoxy → cyclopentadienyl + CO is three elementary steps

1. Electrocyclic **ring contraction** of phenoxy to a **bicyclo[3.1.0] (housane-type)** radical —
   a cyclopropanone ring cis-fused to a cyclopentenyl ring, carbonyl at the cyclopropanone apex.
2. **α-C–C cleavage** of that cyclopropanone ring to a ring-opened **acyl radical** —
   **rate-limiting**.
3. Facile **CO extrusion** from the acyl radical.

It is *not* spiro, the oxygen is never in the ring (no oxepinoxy — that belongs to the
phenyl + O₂ surface), and there is **no ketene intermediate**. Barrier **52 kcal/mol** at
G2M(rcc,MP2) — Liu, Morokuma, Mebel & Lin, *J. Phys. Chem.* **100** (1996) 9314–9322,
[10.1021/jp953566w](https://doi.org/10.1021/jp953566w). See also Olivella, Solé &
García-Raso, *J. Phys. Chem.* **99** (1995) 10549, [10.1021/j100026a018](https://doi.org/10.1021/j100026a018).

**The ~44 vs ~52 kcal/mol gap is falloff, not a PES error.** Carstensen & Dean,
*Int. J. Chem. Kinet.* **44** (2012) 75–89,
[10.1002/kin.20622](https://doi.org/10.1002/kin.20622), abstract verbatim:

> "All methods predict the experimentally determined phenoxy decomposition rate constant to be
> in the falloff region. This explains the almost 10 kcal mol⁻¹ difference between reported
> activation energies and calculated barriers. Both the Lin and Lin (1986) and Frank et al.
> (1994) data can be reproduced within the assumed uncertainty limits without any adjustments
> of the PES."

**Consequence for this family:** the 43.9 kcal/mol training value is an *apparent falloff*
activation energy at ~1 atm, not a barrier. The r117 reactor is at 1 bar, so it is used in the
regime it was fitted for — but the rule is pressure-independent and would be wrong if the deck
moved off ~1 atm. The high-pressure limit is ≈ 9.6 × 10¹³ exp(−53.4 kcal mol⁻¹/RT) s⁻¹.

Shock-tube CO-absorption redetermination: Shu, Herzler, Peukert, Fikri & Schulz,
*Int. J. Chem. Kinet.* **49** (2017) 656–667,
[10.1002/kin.21105](https://doi.org/10.1002/kin.21105) — the DOI cited in the training entry is
correct and is the right paper (anisole/Ar 1000–1270 K, plus allyl phenyl ether as an
independent phenoxy source, PES re-evaluated at G4).

### ✔ RESOLVED 2026-08-03 — the misattributed A factor, corrected

**Ruling (Alon, 2026-08-03):** fix it on the local branch, correct the attribution, cite a
source locator, and state plainly in this report what the value was previously attributed to and
that the attribution was wrong — but correct only what there is source confidence for, and leave
alone anything whose provenance cannot be pinned down, because a confidently-wrong correction in
a shared database is worse than a documented defect.

**What was previously in the database.** `training/reactions.py` entry 1 carried
**`A = 7.4e11 s⁻¹`**, attributed in its `longDesc` to **Lin & Lin, *J. Phys. Chem.* 90 (1986)
425–431**. **That attribution was wrong.** Lin & Lin do not report 7.4e11.

**What it now carries.** **`A = 2.51e11 s⁻¹`** — the value the cited paper actually reports —
with `Ea = 43.9 kcal/mol`, `Tmin/Tmax = 1000–1580 K`, degeneracy and rank all unchanged. Only A
moved, by a factor of **2.95**; the family is correspondingly ~3× slower. Source locator: the
phenoxy decarbonylation channel is Lin & Lin's **reaction 2** (C₆H₅O → c-C₅H₅ + CO), reported in
log form as `k₂ = 10^(11.40 ± 0.20) exp(−(22100 ± 450)/T) s⁻¹`; DOI
[10.1021/j100275a014](https://doi.org/10.1021/j100275a014), confirmed independently via Crossref
and OpenAlex.

**Why this correction is safe to make.** Two independent lines, neither requiring the unconfirmed
part:

1. **Internal consistency.** `10^11.40 = 2.512e11` and `22100 K × R = 43.92 kcal/mol` — which
   reproduces the 43.9 kcal/mol the entry *already* carried. The coded Ea and the log-form
   expression are self-consistent, so the original author plainly had Lin & Lin's expression in
   hand for Ea and paired it with an A factor from somewhere else.
2. **A discriminator that never reads Lin & Lin at all.** Shu et al. (2017) state their measured
   rate exceeds Lin & Lin / Frank et al. / Carstensen & Dean by factors of **6 / 2 / 1.5**.
   Evaluated at 1070 K, mid-range of their phenoxy data:

   | candidate A | k(1070 K) | Shu / k |
   |---|---|---|
   | 2.51e11 | 267.9 s⁻¹ | **5.98** → the Lin & Lin slot |
   | 7.4e11 (old) | 792.9 s⁻¹ | **2.02** → the Frank slot |

   Both close to within 0.02 of the published integers.

**What was deliberately NOT encoded.** The hypothesis that 7.4e11 originates from **Frank,
Herzler, Just & Wahl (1994)** is consistent with the arithmetic above but the primary text was
never accessible (publisher blocked automated retrieval), so it remains **UNCONFIRMED** and is
recorded in the entry as a non-load-bearing note only. The correction stands on the Lin & Lin
value alone. Had the only available fix been "re-cite Frank and keep 7.4e11", the ruling's own
test would have forbidden it.

**Confidence, stated honestly.** The DOI and bibliographic record are CONFIRMED. The expression
`10^(11.40) exp(−22100/T)` was **not read off the primary PDF** — ACS returns 403 to automated
access, and the abstract is indexed by neither Crossref, OpenAlex nor Semantic Scholar. It rests
on multiple independent retrievals plus the arithmetic above. If someone later obtains the PDF
and finds otherwise, this is the paragraph to check first.

**One consequential knock-on.** The entry's "consistency band" paragraph claimed the Lin & Lin
and Shu expressions "agree within a factor of ~2-3 over 1000-1580 K". That was computed against
the *incorrect* A and is false once A is corrected: the true spread is **4.5× at 1000 K rising to
22× at 1580 K** (9.3× at 1200 K). The paragraph has been restated with the correct numbers and an
explanation (the two fits carry different Ea, 43.9 vs 52.7 kcal/mol, because they sample
different falloff regimes). A second stale claim in the same paragraph — "theory places the
rate-limiting barrier at ~54 kcal/mol", cited to Carstensen & Dean — was an *inference* from
their "almost 10 kcal mol⁻¹" sentence rather than a number in the paper; it has been replaced by
the verbatim quotation plus Liu et al.'s independently-published 52 kcal/mol at G2M.

### Original finding, as first reported (2026-08-01)

`training/reactions.py` entry 1 attributes **A = 7.4 × 10¹¹ s⁻¹** to Lin & Lin 1986. **Lin &
Lin do not report that value.** The paper —
*J. Phys. Chem.* **90** (1986) 425–431, [10.1021/j100275a014](https://doi.org/10.1021/j100275a014)
(DOI confirmed; the training entry currently carries no DOI) — reports

> k₂ = 10^(11.40 ± 0.20) exp(−(22,100 ± 450)/T) s⁻¹

i.e. **A = 2.5 × 10¹¹ s⁻¹**, Eₐ = 43.9 kcal/mol, 1000–1580 K. The Eₐ and T range in the training
entry are right; **the A factor is ~3× too high for the cited source.**

7.4 × 10¹¹ is almost certainly **Frank, Herzler, Just & Wahl**, *Symp. (Int.) Combust.* **25**
(1994) 833–840, [10.1016/S0082-0784(06)80717-4](https://doi.org/10.1016/S0082-0784(06)80717-4),
as coded in PAH/aromatics mechanisms. Independent arithmetic check: Shu et al. state their rate
is faster than Lin & Lin, Frank et al., and Carstensen & Dean by factors of 6, 2 and 1.5. At
1070 K, A = 2.5e11 → ratio 5.9 ≈ 6 (Lin & Lin); A = 7.4e11 → ratio 2.0 ≈ 2 (Frank). The
attribution closes exactly on the published factors.

*(As first filed on 2026-08-01 this was reported without changing anything, on the view that
choosing between two defensible literature values was the owner's call. Alon ruled on 2026-08-03
to correct it. **Superseded by the "RESOLVED" section above**, which is the authoritative account;
this paragraph is retained only to show what was originally reported.)*

### (b) Closed-shell cyclohexa-2,4-dien-1-ones do not extrude CO in one step

Ranked fates at 1000–1400 K:

- **C–C homolysis at the sp³ C6 — wins outright.** Reverse of a barrierless radical–radical
  recombination, so Eₐ ≈ BDE, and that bond is doubly resonance-stabilized: **6.1 ± 0.5
  kcal/mol** with ΔG°(diss) = −0.15 kcal/mol for the para-coupled keto dimer of
  2,6-di-*t*Bu-4-MeO-phenoxyl (Wittman, Hayoun, Kaminsky, Coggins & Mayer, *JACS* **135** (2013)
  12956, [10.1021/ja406500h](https://doi.org/10.1021/ja406500h)); ~8 kcal/mol higher for
  less-hindered trialkylphenoxyl keto dimers (Mahoney & Weiner, *JACS* **94** (1972) 585,
  [10.1021/ja00757a044](https://doi.org/10.1021/ja00757a044)). At 1200 K a 20 kcal/mol bond with
  A ~ 10¹⁵ s⁻¹ dissociates at ~10¹²–10¹³ s⁻¹; every competing channel needs ≥ 50 kcal/mol.
- **1,3-H shift to phenol — ~51 kcal/mol**, and **structurally unavailable** to the 6,6-disubstituted
  adducts this model makes: they have no sp³ H, every remaining ring H is vinylic. Zhu & Bozzelli,
  *JPCA* **107** (2003) 3696, [10.1021/jp0212545](https://doi.org/10.1021/jp0212545).
- **1,2-alkyl shift (dienone–phenol rearrangement) — ≳55 kcal/mol** thermally, and the immediate
  product is a carbene, not a phenol. The classical rearrangement is *acid-catalysed*; there is no
  good evidence for a low-barrier neutral thermal version. Chen et al., *Prog. React. Kinet. Mech.*
  **50** (2025) e021, [10.48130/prkm-0025-0021](https://doi.org/10.48130/prkm-0025-0021) (G4, open access).
- **Reversible 6π retro-electrocyclic ring opening to a dienylketene** — thermally real but a
  shuttle, not a sink; the ring-closed form is far more stable. Koch, Blanch & Wentrup,
  *J. Org. Chem.* **79** (2014) 6978, [10.1021/jo5011087](https://doi.org/10.1021/jo5011087).
  No confirmed barrier for the parent — do not quote one.
- **Retro-Diels–Alder — not a channel** for the monomer; no valid disconnection that doesn't break
  the C=O.

**One-step CO extrusion is a convenient fiction.** Every computed surface routes it through the
same bicyclic ring-contraction motif as the radical case, and a one-step cheletropic CO
extrusion from a six-membered dienone is **orbital-symmetry-forbidden** (the clean concerted
cheletropic decarbonylations are bicyclo[2.2.1]hept-2-en-7-ones and cyclopent-3-en-1-ones —
different geometry). Xu & Lin, *JPCA* **110** (2006) 1672,
[10.1021/jp055241d](https://doi.org/10.1021/jp055241d) (G2M//B3LYP) put the highest TS ≈ 57
kcal/mol above the dienone — *above* the ~51 kcal/mol retro-tautomerization, so even the
unsubstituted dienone preferentially goes **back to phenol** rather than losing CO. Chen et al.
(2025, G4) find **three** elementary steps, with CO leaving from the *cyclized* species, never
from the dienone.

Phenol → cyclopentadiene + CO via cyclohexadienone *has* been observed directly (Scheer,
Mukarakate, Robichaud, Nimlos, Carstensen & Ellison, *J. Chem. Phys.* **136** (2012) 044309,
[10.1063/1.3675902](https://doi.org/10.1063/1.3675902)) and modern models (CRECK; Pratali Maffei
et al., *Proc. Combust. Inst.* **40** (2024) 105272,
[10.1016/j.proci.2024.105272](https://doi.org/10.1016/j.proci.2024.105272)) do carry a net
channel — but as **lumped multi-well master-equation channels over a PES containing the
bicyclic**, not as elementary steps. Encoding that as one elementary step in a rate-rule
database misassigns both the A factor and the barrier. This is exactly the failure mode the
dispatch named, and it is why no such family was written.

**Citations not eyeballed** (searched and cross-checked, but publisher access was blocked):
Shu et al.'s exact Arrhenius parameters; the attribution of 7.4 × 10¹¹ to Frank et al.;
Carstensen & Dean's specific computed barrier; Xu & Lin's 75.8 kcal/mol figure; Olivella's
numerical barriers.

---

## Verification

`testing/test_aryl_decarbonylation.py` — 19 tests, all passing against this worktree's
`input/` tree (`rmg_env`, RMG-Py `polymer` branch at `dfc4df868`):

- 1 atomtype-tree assertion: `Cb`/`Cbf` are not descendants of `Cd` (the direct refutation).
- 6 positive substrates: every aryloxy-type radical above matches and releases CO.
- 12 negative substrates: benzaldehyde, acetophenone, the dispatch's closed-shell dienone,
  2,4-cyclohexadien-1-one, cyclohexanone, cyclopentanone, acetone, phenol, benzene, a
  carbonyl-free cyclohexadienyl radical, and r117 species `125407` and `125409` — **zero**
  over-matches.

The negatives matter more than the positives here: they are what would break first if anyone
acts on the refuted diagnosis and widens the template to admit closed-shell dienones.

## Remaining work

Questions this dispatch stopped on rather than answering:

1. **Why r117 actually made no CO — not closed, and reassigned.** The leading hypothesis
   (decarbonylation generated into the edge on iteration 0 from the `1e-12` cresoxy seeds, never
   promoted to the core) needs `RMG.log` (31 MB) or the iteration-0 edge listing, both on zeus.
   **First thing to check in that log: whether `Aryl_Decarbonylation` appears in the
   loaded-families list at all**, since zeus carries its own RMG-database checkout and this
   dispatch could not confirm it was at or past `e573fc979` (2026-07-22) when r117 launched on
   ~2026-07-29. If that checkout was stale, the conclusion flips from "loaded but never matched"
   to "never loaded", and the whole r117 analysis changes. **Handed to a separate dispatch with a
   narrow zeus allowance (ruling 2026-08-03); deliberately not attempted here.**
2. ~~The A-factor discrepancy is flagged, not fixed.~~ **DONE 2026-08-03** — corrected to
   `2.51e11` under Alon's ruling; see the "RESOLVED" section. The Frank et al. attribution
   remains unconfirmed and was deliberately not encoded.
3. **Pressure dependence.** The rule is a ~1 atm falloff fit presented as pressure-independent.
   Fine for the 1 bar r117 reactor, wrong off it. Whether to carry the PLOG/high-pressure form
   (k∞ ≈ 9.6 × 10¹³ exp(−53.4 kcal mol⁻¹/RT) s⁻¹) is a scope decision not taken here.
4. **Whether the dienone adducts actually redissociate in a run.** The families are loaded and
   engage the adducts when probed, but the real risk is thermochemical: a group-additivity
   estimate will not know that this C–C bond is worth 6–20 kcal/mol rather than ~70. If RMG
   assigns it a normal C–C BDE, the adducts are an artificial sink no family change can fix.
   This is the most likely place the next real defect lives.
5. **No run was launched to confirm any of this**, per the dispatch's absolute limit.
   Verification here is template-matching and unit tests only.

## What was NOT done

No RMG or ARC run was launched; no scheduler command was issued; no `ssh`. Nothing under
`/home/alon/runs/` was modified. `/home/alon/Code/RMG-Py` and `/home/alon/Code/CKMG` were read
only. Nothing was pushed; no PR was opened; the branch is local and unmerged. No CO was added
to any mechanism by hand.
