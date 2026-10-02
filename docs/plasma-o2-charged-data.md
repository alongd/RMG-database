# Oxygen-ion data for the Ar/O2 arm

## Admission, state and units

All five added thermo entries use gas, 1 bar and the **ion convention**:
the explicit electron contributes zero H, S and Cp. For signed charge q,
JANAF electron-convention Hf is converted by Hf_IC = Hf_EC - q(5/2)RT.
Anions therefore ADD 6.197392574 kJ/mol at 298.15 K; cations subtract it.
Species entropy and heat capacity stay unchanged. ThermoData entries anchor
H298/S298 at literal 298 K, so the first tabulated Cp segment supplies the
documented 298-to-298.15 K coordinate conversion. O− instead transcribes a
published NASA7 model, with an explicit 0.15 K analytical reference extension.
No new fit, averaging between sources, group estimate or QM calculation was made.

P means primary full text/table read, A means primary abstract read, S means
secondary coefficient. A full read of a model's compiled reaction table does
not upgrade the underlying coefficient to P. All retrievals: 2026-10-02.
The published experimental authors' fitting procedures are source provenance;
none was repeated or changed here.

O+(4S) uses the quartet graph, distinct from PlasmaAir's existing doublet Op.
Ars uses the existing PlasmaArgon triplet graph. Its thermo in
`PlasmaExcitedNeutralThermo` is **3P2 / Paschen 1s5**, standing in for
the source's **1s5/1s3 kinetic lump**. This is an explicit mapping assumption:
1s3 is 3P0, and its different energy/statistical weight are not represented
by the 3P2 thermo. No population weighting or state-resolved rates are
inferred. A state-resolved treatment would need separate sourced species.

## Thermo: one row per added entry

Values below are the **loaded library data** at 298.15 K, after the stated
conversion. H is kJ/mol; S and Cp are J/(mol K). The 298.15 K JANAF rows are
the source's conventional room-temperature reference, with literal 298 K
runtime values shown separately below.

| Entry / ion | Hf(0) | H_IC(298.15) | S(298.15) | Cp(298.15) | Source, location, grade | Load check |
|---|---:|---:|---:|---:|---|---|
| [Op] | 1560.733000 | 1562.588607426 | 154.959000000 | 20.786000000 | [JANAF SRD13, Fourth Edition, content 1998](https://janaf.nist.gov/tables/O-002.txt), O-002, 0/298.15/400 K rows; **P** | PASS: source checks and actual production NASA H/S/Cp at both T; errors below |
| [O2p] | 1164.700000 | 1164.690607426 | 206.215000000 | 29.195000000 | [JANAF SRD13, Fourth Edition, content 1998](https://janaf.nist.gov/tables/O-030.txt), O-030, 0/298.15/400 K rows; **P** | PASS: source checks and actual production NASA H/S/Cp at both T; errors below |
| [Om] | 105.814000 | 108.043119635 | 157.796295629 | 21.685312872 | [Goos/Burcat/Ruscic BURCAT.THR](https://respecth.elte.hu/burcat/BURCAT.THR.txt), species last added 3 January 2023, O− g 1/97; **P published McBride polynomial table**, independent JANAF O-003 checks | PASS: exact coefficients, reference conversion, JANAF comparison and production NASA |
| [O2m] | -42.464000 | -42.395607426 | 209.591000000 | 30.453000000 | [JANAF SRD13, Fourth Edition, content 1998](https://janaf.nist.gov/tables/O-031.txt), O-031, 0/298.15/400 K rows; **P** | PASS: source checks and actual production NASA H/S/Cp at both T; errors below |
| [O3m] | -58.470000 | -60.821325783 | 247.967869804 | 41.931351573 | [ATcT v1.156](https://atct.anl.gov/Thermochemical%20Data/version%201.156/species/?species_number=298), Ozonide selected table, Hf(0); [Arnold 1994](https://doi.org/10.1063/1.467745), pp. 917–918 Table V; **P constants; DERIVED thermal functions** | PASS: source checks and actual production NASA H/S/Cp at both T; errors below |

### Reproduced source and actual production values

H is kJ/mol; S and Cp are J/(mol K). Reference H(T) is the fixed-reference
IC formation enthalpy at 298.15 K plus the species thermal increment.
JANAF's delta-f H(T) also changes elemental/electron reference states and
is not this RMG H(T). O3− references are independently evaluated RRHO values.

| Entry | T / K | Library H | Source H | Library S | Source S | Library Cp | Source Cp |
|---|---:|---:|---:|---:|---:|---:|---:|
| [Op] | 298.15 | 1562.588607426 | 1562.588607426 | 154.959000000 | 154.959000000 | 20.786000000 | 20.786000000 |
| [Op] | 400.0 | 1564.705661526 | 1564.705607426 | 161.067336747 | 161.067000000 | 20.786000000 | 20.786000000 |
| [O2p] | 298.15 | 1164.690607426 | 1164.690607426 | 206.215000000 | 206.215000000 | 29.195000000 | 29.195000000 |
| [O2p] | 400.0 | 1167.681021876 | 1167.680607426 | 214.840547873 | 214.839000000 | 29.573000000 | 29.573000000 |
| [Om] | 298.15 | 108.043119635 | 108.043392574 | 157.796295629 | 157.790000000 | 21.685312872 | 21.692000000 |
| [Om] | 400.0 | 110.233830370 | 110.234392574 | 164.119484788 | 164.114000000 | 21.361412580 | 21.364000000 |
| [O2m] | 298.15 | -42.395607426 | -42.395607426 | 209.591000000 | 209.591000000 | 30.453000000 | 30.453000000 |
| [O2m] | 400.0 | -39.216994401 | -39.216607426 | 218.751403458 | 218.752000000 | 31.962000000 | 31.962000000 |
| [O3m] | 298.15 | -60.821325783 | -60.821325783 | 247.967869804 | 247.967869804 | 41.931351573 | 41.931351573 |
| [O3m] | 400.0 | -56.313685741 | -56.310974367 | 260.941508823 | 260.949277055 | 46.409911890 | 46.409911890 |

The following values pass through `get_thermo_data` **and**
`process_thermo_data`; they are the NASA that the species/model carries.
All five also pass `NASA.to_cantera()`. Library lookup alone was insufficient.

| Entry | T / K | Production NASA H | Source H | Production NASA S | Source S | Production NASA Cp | Source Cp |
|---|---:|---:|---:|---:|---:|---:|---:|
| [Op] | 298.15 | 1562.588607449 | 1562.588607426 | 154.959000079 | 154.959000000 | 20.786156545 | 20.786000000 |
| [Op] | 400.0 | 1564.705677494 | 1564.705607426 | 161.067382829 | 161.067000000 | 20.786156545 | 20.786000000 |
| [O2p] | 298.15 | 1164.690548755 | 1164.690607426 | 206.214803168 | 206.215000000 | 28.804182142 | 29.195000000 |
| [O2p] | 400.0 | 1167.662777419 | 1167.680607426 | 214.784832910 | 214.839000000 | 29.602299050 | 29.573000000 |
| [Om] | 298.15 | 108.043119635 | 108.043392574 | 157.796295629 | 157.790000000 | 21.685312872 | 21.692000000 |
| [Om] | 400.0 | 110.233830370 | 110.234392574 | 164.119484788 | 164.114000000 | 21.361412580 | 21.364000000 |
| [O2m] | 298.15 | -42.395592731 | -42.395607426 | 209.591049299 | 209.591000000 | 30.550762463 | 30.453000000 |
| [O2m] | 400.0 | -39.220098198 | -39.216607426 | 218.744166735 | 218.752000000 | 31.819947797 | 31.962000000 |
| [O3m] | 298.15 | -60.821333327 | -60.821325783 | 247.967844496 | 247.967869804 | 41.880588582 | 41.931351573 |
| [O3m] | 400.0 | -56.335391437 | -56.310974367 | 260.880614267 | 260.949277055 | 46.113683057 | 46.409911890 |

Three JANAF ThermoData ions retain every source Cp point through 6000 K,
with H/S coordinate shifts explicitly derived at 298 K. Their library
400 K integration errors stay below 2 J/mol and 0.003 J/(mol K).
O− uses the published McBride **NASA7** coefficient table in BURCAT.THR;
the coefficients are transcribed, never fitted here. Its small JANAF
differences reflect that independent published model and fine-structure
splitting, not blending of sources. Cp differs by −0.006687128 at 298.15 K
and −0.002587420 at 400 K; H by −0.272939 and −0.562204 J/mol; S by
+0.006295629 and +0.005484788 J/(mol K). The complete coefficient record,
reference conversion, and every JANAF Cp grid comparison are tested.

Correct classical limits are Cp0/CpInf=2.5R/2.5R for atoms, 3.5R/4.5R
for the diatomic ions, and 4R/7R for nonlinear O3−. Cp0 includes classical
rotation; these are RMG's classical limits, not quantum T→0 rotational
limits or a claim about electronic/dissociation contributions at infinite T.

The pinned RMG still approximates the molecular source curves via Wilhoit.
O2+ production Cp(298.15)=28.804182142 versus JANAF 29.195 (−1.339%);
the previous wrong-limit value was 28.143. Production checks bound each
ion's H, S **and Cp** separately in absolute physical units, with `rel=0`.
Largest H/S errors at the two temperatures are 17.830007 J/mol and
0.054167090 J/(mol K) for O2+, 3.490772 J/mol and 0.007833265 J/(mol K)
for O2−, and 24.417070 J/mol and 0.068662789 J/(mol K) for O3−.
These conversion errors are disclosed approximations; passing the test
does not make the NASA identical to a JANAF/RRHO curve. Tight source/grid
tests separately prevent the conversion tolerances admitting altered data.

### Source coverage and ranges imposed by RMG

| Entry | Published/delivered coverage | Library bounds / K | Production NASA bounds / K | Meaning |
|---|---|---|---|---|
| [Op], [O2p], [O2m] | JANAF 298.15–6000 K, derived reference extension to 298 | 298–6000 | 100–5000 | Whole source grid retained; RMG forces conversion bounds |
| [Om] | Published NASA7 298.15–6000 K, analytical reference extension to 298 | 298–6000 | 298–6000 | RMG preserves sourced library NASA; no JANAF upper range lost |
| [O3m] | RRHO delivery 298.15–1000 K, derived reference extension to 298 | 298–1000 | 100–5000 | **Use only 298–1000 K**; metadata above 1000 is engine extrapolation, not source coverage |

The cause is read-only `rmgpy/thermo/thermoengine.py:process_thermo_data`:
it calls `ThermoData.to_wilhoit(B=1000)` followed by
`to_nasa(Tmin=100,Tmax=5000,Tint=1000)`. A library NASA is kept instead.
Equal atomic Cp0/CpInf take a constant-Cp Wilhoit shortcut, which erased
O− fine structure; the published NASA7 entry avoids that production defect.
O+ still uses the source ThermoData: its delivered JANAF Cp(5000 K) is
21.351 J/(mol K), but production NASA gives the constant 2.5R =
20.786156545 J/(mol K), a −2.645513% loss of the high-temperature electronic
contribution. The production-path test pins this 5000 K source row and loss;
it does not claim that the constant-Cp conversion reproduces high-T JANAF.
NASA9 was not shipped because this engine's Chemkin/Cantera exports cannot
represent it. No new polynomial or engine change was made. RMG also derives
the species conformer E0 from Wilhoit; the tabulated library E0 must not be
confused with that downstream extrapolation. None of these engine metadata
or extrapolations establishes additional source validity.

### O3− derivation and independent cross-check

ATcT v1.156 Ozonide gives Hf(0)=−58.47 kJ/mol and mass 47.99875 g/mol.
[Arnold, Xu, Kim and Neumark, JCP 101 (1994) 912–922](https://doi.org/10.1063/1.467745),
full text read from the [author archive](https://bromine.cchem.berkeley.edu/grppub/pes20.pdf):
p. 917 and conclusion p. 921 give r=1.36±0.02 Å and angle=111.8±2 degrees;
Table V p. 918's experimental row gives 975±50, 550±50 and 880±50 cm−1.
The 880 constant's footnote attributes it to an unpublished hot spectrum;
the constant itself is published in this primary paper. The geometry text
is used rather than averaging it with the table's 111.7 degree rounding.
No calculated geometry or ab initio frequency row was used.

With ideal-gas translation at 1 bar, a classical nonlinear rigid rotor,
symmetry number 2, electronic degeneracy 2 and these three harmonic modes:

```
theta_i = h*c*100*nu_i/kB; x_i=theta_i/T
qtrans=(2*pi*m*kB*T/h^2)^(3/2)*kB*T/1e5
qrot=sqrt(pi)*T^(3/2)/(2*sqrt(theta_A*theta_B*theta_C))
S/R=ln(qtrans)+5/2+ln(qrot)+3/2+ln(2)
    +sum(x_i/(exp(x_i)-1)-ln(1-exp(-x_i)))
[H(T)-H(0)]/R=4*T+sum(theta_i/(exp(x_i)-1))
Cp/R=4+sum(x_i^2*exp(-x_i)/(1-exp(-x_i))^2)
Hf_IC(298.15)=-58.47+10.673174217-(3/2)*8.683
              =-60.821325783 kJ/mol
```

JANAF O-029's 0 K row supplies H(O2,298.15)−H(O2,0)=8.683 kJ/mol.
Principal moments, rotational temperatures, all constants and full formulas
are recorded in the entry longDesc and `docs/oxygen-ion-data/derive_o3.py`. Equal oxygen mass shares
are used with the ATcT total mass. Exact SI constants are taken from the
[BIPM defining-constants table](https://www.bipm.org/en/measurement-units/si-defining-constants).

The independent ATcT 298.15 K value is −60.83±0.21 kJ/mol: the derived result
differs by +0.008674217 kJ/mol. It is a cross-check, never an averaged input.
The 400 K reference is an independently evaluated **derived** RRHO row,
not a published ion thermal table. Stored Cp points are calculated 298.15–1000 K
values plus the explicit 298 K first-segment reference extension; the interval is a delivery range, not an experimentally established
validity range. Grid integration error is below 0.02 kJ/mol in H and
0.05 J/(mol K) in S at 400 K. Spectroscopic uncertainty, unprovided anion
anharmonicity and omission of excited electronic states limit accuracy.
The complete reconstruction is executable in-repo; the production values are
recorded at `/home/alon/runs/i316-o2-charged/rework3-load-check.stdout.log`.

## Kinetics: one row per added entry

Library: `PlasmaOxygenHeavy`. All channels are irreversible, use gas T only,
and balance atoms and explicit charge. The explicit electron is a species
with default reaction `electrons=0`, so it is not also implicit. Two-body
k uses particle m³/s, three-body k uses particle m⁶/s. Stored RMG A uses
cm³/(mol s) or cm⁶/(mol² s): multiply by NA*1e6 or NA²*1e12,
NA=6.02214076e23 mol−1. Each rate passed independent particle-unit comparison
at 298, 298.15 and 400 K. Entry 101 also passed at 1400 K in the test suite.

For the power laws below k=A*(T/300)^n. `T` is gas temperature in kelvin.

| Index / channel | Particle A, n or full expression | k(298 K) | k(400 K) | Source, location, grade | Load check |
|---|---|---:|---:|---|---|
| 31: O2p + O- => O2 + O | A=2.6e-14, n=-0.44 | 2.607663474e-14 | 2.290869256e-14 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), V-31, p. 17 → RH-16-2004; **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 32: Op + O- => O + O | A=4e-14, n=-0.43 | 4.011521621e-14 | 3.534567946e-14 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), V-32, p. 17 → RH-16-2004; **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 33: O + O- => O2 + e- | A=2.3e-16, n=0.0 | 2.3e-16 | 2.3e-16 | [Belostotsky 2005](https://doi.org/10.1088/0963-0252/14/3/016), Table 1 R2 p. 540; **P**, (2.3±0.5)e−10 cm³/s | PASS: parameters, rates, states, atoms, charge, irreversible |
| 34: O2 + Op => O + O2p | A=2.1e-17, n=-0.5 | 2.107035196e-17 | 1.818653348e-17 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), V-34, p. 17 → Eliasson/Kogelschatz KLR-11C (1986); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 38: O2p + O2- => O2 + O2 | A=2.01e-13, n=-0.5 | 2.016733687e-13 | 1.740711062e-13 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), V-38, p. 17 → Eliasson/Kogelschatz KLR-11C (1986); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 39: Op + O2- => O2 + O | A=2.7e-13, n=-0.5 | 2.709045251e-13 | 2.33826859e-13 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), V-39, p. 17 → [Kossyi 1992](https://doi.org/10.1088/0963-0252/1/3/011); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 40: O + O2- => O2 + O- | A=3.31e-16, n=0.0 | 3.31e-16 | 3.31e-16 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), V-40, p. 17 → Eliasson/Kogelschatz KLR-11C (1986); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 41: O2a + O2- => O2 + O2 + e- | A=7e-16, n=0.0 | 7e-16 | 7e-16 | [Midey/Dotan/Viggiano 2008](https://doi.org/10.1021/jp710539s), primary abstract; **A**, approximately 7e−10 cm³/s, 200–700 K | PASS: parameters, rates, states, atoms, charge, irreversible |
| 42: O2 + O- => O3 + e- | A=5e-21, n=0.0 | 5e-21 | 5e-21 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), V-42, p. 17 → [Kossyi 1992](https://doi.org/10.1088/0963-0252/1/3/011); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 52: O + O2- => O3 + e- | A=3.3e-16, n=0.0 | 3.3e-16 | 3.3e-16 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), V-52, p. 17 → Fehsenfeld et al. 1967 JCP 46 2802; **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 58: O2p + O- => O + O + O | A=2.6e-14, n=-0.44 | 2.607663474e-14 | 2.290869256e-14 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), V-58, p. 17 → RH-16-2004; **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 67: O2p + O2- => O2 + O + O | A=1.01e-13, n=-0.5 | 1.013383594e-13 | 8.746856578e-14 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), V-67, p. 17 → Eliasson/Kogelschatz KLR-11C (1986); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 80: O2 + Op + O- => O2 + O2 | A=2.1e-37, n=-2.5 (m⁶/s) | 2.135412454e-37 | 1.022992508e-37 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), VI-80, p. 18 → Eliasson/Kogelschatz KLR-11C (1986); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 81: O2 + O2p + O- => O2 + O3 | A=2.01e-37, n=-2.5 (m⁶/s) | 2.043894778e-37 | 9.791499722e-38 | [Kemaneci v1](https://arxiv.org/abs/1612.07268), VI-81, p. 18 → Eliasson/Kogelschatz KLR-11C (1986); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 101: Arp + O2 => Ar + O2p | 4.9e−17*(300/T)^0.78 + 9.2e−16*exp(−5027.6/T) | 4.925636454e-17 | 3.915429063e-17 | [Kutasi 2010](https://doi.org/10.1088/0022-3727/43/5/055201), p. 2 sec. 3 ref. 23 → [Midey 1998](https://doi.org/10.1063/1.477142); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 102: Arp + O => Ar + Op | A=1.21e-17, n=0 | 1.21e-17 | 1.21e-17 | [Dong v1](https://arxiv.org/abs/2601.08138), A1 row 35, p. 21 → [Liu 2015](https://doi.org/10.1088/0963-0252/24/2/025035); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 103: Ars + O2 => Ar + O2 | A=1.12e-15, n=0 | 1.12e-15 | 1.12e-15 | [Dong v1](https://arxiv.org/abs/2601.08138), A1 row 31, p. 21 → [Liu 2015](https://doi.org/10.1088/0963-0252/24/2/025035); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 104: Ars + O2 => Ar + O + O | A=5.8e-17, n=0 | 5.8e-17 | 5.8e-17 | [Dong v1](https://arxiv.org/abs/2601.08138), A1 row 33, p. 21 → [Liu 2015](https://doi.org/10.1088/0963-0252/24/2/025035); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |
| 105: Ars + O => Ar + O | A=8.1e-18, n=0 | 8.1e-18 | 8.1e-18 | [Dong v1](https://arxiv.org/abs/2601.08138), A1 row 34, p. 21 → [Liu 2015](https://doi.org/10.1088/0963-0252/24/2/025035); **S** | PASS: parameters, rates, states, atoms, charge, irreversible |

### Selection, reversibility and rate limitations

- Kemaneci's complete model tables were read, but their compiled rates retain
  S. RH-16-2004, ABB KLR-11C, Kossyi's primary full text and Fehsenfeld's
  original detachment measurement were not recovered. These are upgrade gaps,
  not grounds to fabricate P provenance.
- Belostotsky's full paper was read from the author's open university
  publication archive. Its published measured result includes a documented
  correction; the correction was not newly fitted here. The gas T is measured
  in the experiment; no separate broad thermal validity range is claimed.
- Midey 2008's primary author/institution abstract was read, full text unavailable
  at ACS. Its O2−+O2(a) value replaces Kemaneci's older 2e−16 m³/s value;
  approximately 7e−16 m³/s is transcribed without averaging. Abstract location:
  [author record](https://cris.openu.ac.il/en/publications/temperature-dependences-for-the-reactions-of-osup-sup-and-o-sub2s/).
  Associative detachment was the only observed O2− branch. Its source interval
  is 200–700 K.
- Kutasi's open author full text gives the two-term Ar++O2 expression cited to
  Midey 1998. Original measurement full text was unavailable (publisher 403);
  coefficient grade remains S. Preserve 300–1400 K bounds. Evaluation at 298 K
  is flagged extrapolation, not a verified source interval. Do not average
  with Dong's 1.2e−17 m³/s. MultiArrhenius encodes one published sum, not two
  independently counted channels. The pinned runtime's R=8.314472 is used for
  Ea=R_runtime*5027.6=41801.8394272 J/mol to preserve the source exponent.
- Dong's complete Ar/O2 model manuscript was read, including its explicit
  Ar* level lump. Its four added compiled coefficients remain S. Liu 2015's
  publisher full text was unavailable. The author's public publication list
  links the PDF but requires a CAPTCHA; no restricted access was bypassed.
- The two O2++O− channels are transcribed exactly from the source model.
  Original branch measurements were not recovered; both remain S. No total
  rate was newly split or averaged. Other mutual-neutralisation coefficients
  differ between models; these entries preserve the Kemaneci set rather than
  averaging competing models. These source/product-state uncertainties remain.
- O−+O2 detachment coefficients span orders of magnitude across compilations.
  Entry 42 preserves the explicitly traced 5e−21 Kossyi/Kemaneci channel, S;
  no independently validated room-temperature replacement was recovered.
- Three-body entries 80/81 contain O2 explicitly with ordinary Arrhenius;
  neither a generic collider nor Ar efficiency was inferred.
- PlasmaAir 13 is a reverse charge-transfer channel with a different (doublet)
  Op graph; PlasmaAir 66 already supplies O−+O2(a)→O3+e. That existing channel
  was not duplicated or rebranched. Avoid loading overlapping channels from
  both libraries without selecting them. Midey's other O−+O2(a) branches
  cannot all be specified from its abstract alone.
- No unstated independent Tmin/Tmax is inferred for the other source laws.
  An unbounded Arrhenius input is not evidence of universal thermal validity.

## Reduced ion mobilities (report only)

Read the [LXCat Viehland database](https://nl.lxcat.net/Viehland), Gaseous Ion
Transport and Rate Coefficient Database, Software Release 4.1 (March 2006),
as regularly updated, retrieved 2026-10-02. The selected full numerical export
is `/home/alon/runs/i316-o2-charged/sources/lxcat-mobility.txt`, including dataset timestamps and bibliography.
Database citation: Viehland & Kirkpatrick, Int. J. Mass Spectrom. Ion Proc.
149/150 (1995) 555. No mobility was written into the database or reactor deck.

**K0 values below are sampled at the stated E/N**, not extrapolated E/N=0
limits. The range covers the entire retrieved dataset. 1 Td=1e−21 V m².
Divide cm²/(V s) by 10000 to obtain m²/(V s). No 300-to-298 K correction,
field extrapolation, source averaging or Langevin estimate was made.
LXCat ion-state labels are reproduced verbatim; their fine-state resolution
was not independently established from the original measurements.

| Ion / bath | T / K | Selected E/N / Td | K0 / cm² V−1 s−1 | K0 / m² V−1 s−1 | Full E/N range / Td | Source/location/grade |
|---|---:|---:|---:|---:|---|---|
| O2+ / Ar | 300 | 8 | 2.57 | 2.57e−4 | 8–240 | LXCat Ellis compiled block, O2+/Ar; Ellis et al. 1976 [doi:10.1016/0092-640X(76)90001-2](https://doi.org/10.1016/0092-640X(76)90001-2); **S** |
| O+(4S3/2) / Ar | 300 | 5 | 3.43 | 3.43e−4 | 5–250 | same Ellis block, 16O+(4S3/2)/Ar; **S** |
| O− / Ar | — | — | **not found** | — | — | absent from selected Viehland catalog; no estimate |
| O2− / Ar | — | — | **not found** | — | — | absent from selected Viehland catalog; no estimate |
| O2+ / O2 | 300 | 4 | 2.23 | 2.23e−4 | 4–500 | same Ellis block, O2+/O2; **S** |
| O+ / O2 | — | — | **not found** | — | — | absent from selected Viehland catalog; no estimate |
| O−(2P1/2) / O2 | 300 | 4 | 3.20 | 3.20e−4 | 4–160 | same Ellis block, 16O−(2P1/2)/O2; **S** |
| O2− / O2 | 300 | 3 | 2.17 | 2.17e−4 | 3–140 | same Ellis block, O2−/O2; **S** |
| O+(4S3/2) / Ar | 293 | 100 | 2.92 | 2.92e−4 | 100–300 | LXCat Viehland & Mason 1995 compiled block, [doi:10.1006/adnd.1995.1004](https://doi.org/10.1006/adnd.1995.1004); **S**; different high-field regime |
| O2+ / O2 raw | 300 | 3.91 | 2.253 | 2.253e−4 | 3.91–549.17 | LXCat raw Georgia Tech 1970–1974 report block; **P database table**, original technical reports not individually read |
| O2− / O2 raw | 300 | 3.10 | 2.177 | 2.177e−4 | 3.10–140.49 | same LXCat raw block; **P database table**, original technical reports not individually read |
| O−(2P1/2) / O2 raw | 300 | 3.97 | 3.205 | 3.205e−4 | 3.97–174.85 | same LXCat raw block; **P database table**, original technical reports not individually read |

The primary O+/Ar paper [Danailov et al. 2008](https://doi.org/10.1063/1.2898523)
was read at abstract level, without a numeric low-field value or full curve:
it therefore does not supersede the tabulated values. The O2−/Ar dense-gas
study [arXiv:2210.01687](https://arxiv.org/abs/2210.01687) was read but covers
180–300 K and very high gas densities; no suitable dilute-gas room-temperature
numeric table was recovered. Its graphs were not estimated or extrapolated.
The Ellis and Viehland compilation articles remain unread; their DOIs are
provided rather than implying primary measurement provenance.

## Reproduction and load check

Both scripts are shipped in-repo and derive their root from their own location:

```bash
cd /home/alon/Code/RMG-database-i316-o2-charged
PYTHONPATH=/home/alon/Code/RMG-Py-plasma /home/alon/anaconda3/envs/rmg_env/bin/python docs/oxygen-ion-data/load_check.py
/home/alon/anaconda3/envs/rmg_env/bin/python docs/oxygen-ion-data/derive_o3.py
PYTHONPATH=/home/alon/Code/RMG-Py-plasma /home/alon/anaconda3/envs/rmg_env/bin/python -m pytest test/test_plasma_oxygen_charged.py -q -p no:cacheprovider
```

The first script asserts the source transcription, actual production NASA
H/S/Cp at 298.15 and 400 K, parameter/entry inventories and state graphs,
then prints their measurements as JSON. It reproduces **19 rejected A=0
mutations, 19 rejected A×2 mutations, 57 rejected n/Ea/T0 mutations,
the O2→O2(a) state swap, and doubled O3− Cp at 1000 K**. Particle-rate
comparisons use finite-positive assertions and relative-only `abs=0`.
Graphs are compared with the existing PlasmaAir/PlasmaArgon dictionaries,
including multiplicity, radicals, lone pairs, charges and bonds; atom
renumbering is immaterial. O2a matches PlasmaAir `O2s`; quartet Op is pinned
separately from legacy doublet Op. The electron reuses the exact existing
PlasmaAir/PlasmaArgon adjacency `1 e u1 p0 c-1` (multiplicity 2). Zero
electron H/S/Cp is a thermochemical reference convention and does not change
its spin graph. Tests load all three libraries and admit every reaction through
`CoreEdgeReactionModel.make_new_reaction` in all six orders. One shared u1
electron remains, and the old u0 graph still fails identity admission.

**Independent-channel admission is preserved on RMG-Py `eccc1938a`.** Heavy
33 associative detachment and PlasmaAir 55 electron-impact attachment remain
independent irreversible reactions with their own directions and gas/electron
temperature rate laws. Six strict regressions assert that both source objects
and their coefficients survive every library order, duplicate marking,
edge-to-core promotion, and `ReactionModel.merge` in both merge orders.

`load_check.py` measures the admitted `model.new_reaction_list` objects, their
provenance/rate classes, pair count and actual detachment indices in all six
orders. Every order retains all four heavy detachment channels (33, 41, 42,
52) and Air 55, initializes PlasmaReactor with one electron, and retains the
focal pair through duplicate marking, edge-to-core promotion, and both merge
orders. The checker emits JSON and exits nonzero on any lost channel. The
obsolete engine proposal was removed after these checks passed. PlasmaAir and
RMG-Py remain untouched.

### Whole-branch reverse-pair scan

The shipped [audit_reverse_pairs.py](oxygen-ion-data/audit_reverse_pairs.py)
historically inventoried all 190 library files / 35,278 active source entries,
loaded all 36 libraries with irreversible entries, and examined all 2,454
loaded irreversible reactions on the pre-`eccc1938a` engine. It canonicalized
through actual model species admission, including state identity, colliders
and per-side electron counts. The criterion was two opposite **irreversible**
channels in different libraries, not an ordinary reversible reaction's
thermodynamic reverse. That run found these three pairwise exposures; the
current six-order check supersedes its focal-pair result:

| First library / index / direction | Opposite library / index / direction | Reproduced result |
|---|---|---|
| JetSurF1.0 / 1435 / `PC12H25O2 => P12OOHX2` | JetSurF2.0 / 1416 / `P12OOHX2 => PC12H25O2` | Second object lost in both orders |
| JetSurF2.0 / 1415 / `PC12H25O2 => P12OOHX2` | JetSurF1.0 / 1436 / `P12OOHX2 => PC12H25O2` | Second object lost in both orders |
| PlasmaAir / 55 / `O2 + e- => O- + O` | PlasmaOxygenHeavy / 33 / `O + O- => O2 + e-` | Historical old-engine exposure; both survive on RMG-Py `eccc1938a` |

The two JetSurF pairs are pre-existing; no additional affected pair involving
the new heavy library was found. PlasmaAir 13 versus heavy 34 shares reversed
stoichiometric labels but uses doublet versus quartet O+, so it is not a
state-identical model reverse pair. The preserved argon same-library 87/89/91
channels are controls for the different same-library path.
The historical full measured results are shipped as
[reverse-pair-audit.json](oxygen-ion-data/reverse-pair-audit.json); captured
streams are `/home/alon/runs/i316-o2-charged/rework3-reverse-audit.stdout.log`
and `.stderr.log`.

The second script recomputes the whole delivered O3− Cp grid and 298 K
anchors from the cited constants, using centre-of-mass coordinates and
principal moments. The test independently derives the moments in closed
form and checks **every** delivered Cp point and all grid H/S values.
Snapshots are cross-checks, never a substitute for this recomputation.

The rework-3 verification streams are in `/home/alon/runs/i316-o2-charged/`:
`rework3-targeted.stdout.log` and `.stderr.log`,
`rework3-load-check.stdout.log` and `.stderr.log`, and
`rework3-o3-grid.stdout.log` and `.stderr.log`. Fresh full base/tip suite
results and the exact summary lines are recorded in `report.md` there.
Archived downloaded source tables/papers remain in `/home/alon/runs/i316-o2-charged/sources/`,
including `BURCAT-20230103.THR` and `lxcat-mobility.txt`; these machine-local
archives are explicitly located and are not required by either shipped script.

## Missing and deliberately unchanged

- **Ar++O−→Ar+O is omitted.** Dong reports 2.7e−17 m³/s; other model tables
  give 2.7e−13 m³/s. The original coefficient and discrepancy were not
  resolved. No guessed correction is admitted.
- **Ar++O2− mutual neutralisation, Ar*+O− detachment, and O2−+O2
  heavy-particle detachment** coefficients were not recovered. They are omitted.
- **Ar third-body mutual neutralisation rates** were not located. O2 collider
  coefficients are not transferred to Ar. Heavy-particle electron-impact
  attachment, detachment and recombination repairs remain outside this task.
- **O−/Ar, O2−/Ar and O+/O2 dilute-gas mobility tables** were not recovered.
  In particular, an O−/Ar mobility needed by the mixed-gas wall guard is still
  missing; these data do not complete the integration mechanism.
- **Original primary coefficients behind retained S rates** remain missing:
  RH-16-2004, ABB KLR-11C, Kossyi 1992, Fehsenfeld 1967, Midey 1998 and Liu
  2015. See the DOI/report identifiers in the rows and longDescs. Publisher
  access failures and the author's CAPTCHA were respected.
- **Full Midey 2008 source, O−+O2(a) branch details and temperature fits** were
  unavailable. The existing PlasmaAir 66 remains unchanged; no new O3 branch
  fraction was invented. The abstract-sourced O2− coefficient remains A.
- **Direct O3− Cp/S thermal table** was not found. The admitted spectroscopy
  calculation supplies the entry, with the explicit RRHO limitations above.
- **State-resolved Ar* quenching and mutual-neutralisation branching** were
  not recovered. The sourced lumps are delivered without new levels or state
  allocations. Ars has sourced 3P2 thermo, with the explicit proxy assumption above.
  The legacy rate-estimation and transport suite failures are reproduced
  baseline limitations and were not repaired here.
- No engine work, electron-impact rates, extra O2 levels, H2/N2 data, reactor
  deck edits, official remote push, or merge into plasma was performed.

## Quartet [Op] versus PlasmaAir's doublet Op

The O2-arm model must carry one atomic O+ ground-state reservoir with the
**quartet [Op]/Op graph** `multiplicity 4; 1 O u3 p1 c+1`. The new heavy
library's Op is graph-identical to [Op] in PlasmaThermo, so that sourced
ground-ion thermo is selected. PlasmaAir currently defines Op as
`1 O u1 p2 c+1` (inferred multiplicity 2). RMG treats those as distinct
species; matching the text label does not merge them or select quartet
thermo for the doublet. Loading both dictionaries as-is would create an
additional, physically unresolved doublet ion reservoir.

[NIST's O II energy-level table](https://physics.nist.gov/PhysRefData/Handbook/Tables/oxygentable6.htm),
MKM93 rows, identifies 2s²2p³ 4S°3/2 at 0 cm−1. The lowest doublets are
2D° at 26810.55/26830.57 cm−1 and 2P° at 40468.01/40470 cm−1.
Thus a doublet graph cannot encode ground-state O+. Multiplicity alone
also cannot say whether it denotes 2D or 2P. No term-resolved energy or
excitation/quenching scheme accompanies PlasmaAir's generic Op label.

Evidence for a **misencoded intended ground ion**, rather than an intentional
doublet state: PlasmaAir reaction 19 labels its channel ordinary O ionization
and uses 13.6254 eV, close to the neutral oxygen ground-ion limit
109837.02 cm−1 in [NIST's O I table](https://physics.nist.gov/PhysRefData/Handbook/Tables/oxygentable5.htm)
(about 13.618 eV). Its generic Op charge-transfer/recombination channels
also do not designate a 2D/2P state. A state-resolved lowest-doublet
threshold would include approximately 3.324 eV additional excitation.
This is an inference from the graph, rates and primary level tables;
the originating PlasmaAir authors' intent was not independently established.

**Recommended separate fix:** audit every PlasmaAir Op channel against its
source state assignment, change intended ground Op consistently to the
quartet graph, bind the sourced [Op] thermo, and test graph identity and
cross-library duplicate channels before loading both libraries together.
If a source truly resolves O+(2D) or O+(2P), give that state a distinct
label, separately sourced thermo and state-specific rates. Until that
audit, use the new quartet reservoir for the O2 arm and explicitly exclude
legacy doublet Op channels; retain unrelated PlasmaAir channels only after
checking overlap. This rework leaves **all PlasmaAir files unchanged**.
