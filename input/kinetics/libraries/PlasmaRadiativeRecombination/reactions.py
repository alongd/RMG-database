#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaRadiativeRecombination"
shortDesc = u"Radiative recombination of atomic cations: Badnell (2006) fits, plus one transcribed literature row"
longDesc = u"""
Radiative recombination of a monatomic cation with a free electron, one recombination
stage:

    A+ + e-  =>  A + hv

carried in RMG's database representation as ``A+ => A`` with ``electrons = -1``. Unlike
electron-impact ionization, this channel has no spectator electron: the incident electron
is captured and does not come out again, so the single electron is both the whole incident
order and the whole net change. That is the degenerate case where a one-sided declaration
would have sufficed, and it is why this library's placement declaration reads
``(reactant_count, product_count) = (1, 0)`` - the same numbers attachment declares, for
the same structural reason and different chemistry.

The photon is not represented. RMG has no photon species, and ``hv`` carries neither
charge nor mass, so no balance check misses it. What IS lost by omitting it is the energy
sink: this reaction removes 5.392 eV per event from the electron population and the model
has nowhere to put it. `PlasmaReactor` prescribes ``Te`` rather than solving an electron
energy equation, so that omission costs nothing here - but it would matter to any reactor
that closed the electron energy balance, and it is recorded rather than assumed away.

WHAT THIS CHANNEL IS, AND WHAT IT IS NOT
----------------------------------------
**It is not the inverse of electron-impact ionization.** A binding project ruling forbids
treating the reverse of a process as the same elementary channel run backwards, and this
is the case that makes the rule concrete. The physical inverse of
``Li + e- => Li+ + 2 e-`` is **three-body (collisional) electron-ion recombination**,
``Li+ + 2 e- => Li + e-`` - same participants, run the other way, third order, with the
second electron carrying off the binding energy. Radiative recombination is a *different
forward channel*: second order, with a photon carrying the energy instead. Its own inverse
is photoionization ``Li + hv => Li+ + e-``, which needs a radiation field the reactor does
not have. All three are distinct processes with distinct rates.

**It is therefore not the dominant electron sink.** At every electron density this campaign
has named, three-body recombination outruns radiative recombination - by ~2x at
n_e = 1e10 cm^-3 and by ~9x at 1e14 cm^-3, at Te = 1 eV. Three-body recombination has no
shipped fit anywhere in this database (``input/kinetics/`` holds ``voronov.yaml`` and
``badnell.yaml`` and nothing else), so it is not entered here and no rate for it is
authored. The measurements, and what would be needed to close that gap, are in
``docs/i119-recombination-loss.md``.

WHY A LIBRARY AND NOT A FAMILY
------------------------------
The same argument that made ionization a library, and it transfers without weakening;
the long form is ``docs/i114-ionisation-owner.md``. The Badnell fit is indexed by
``(Z, N)`` - a nuclear charge and an electron count, an *atomic identity*, not a molecular
group - and its five parameters (A, B, T0, T1, and the optional C, T2) describe one ion's
recombination cross-section summed over final states. There is no group-additivity trend to
interpolate along, so an averaged "estimate" between two elements' fits would be a
fabricated number rather than an uncertain one. RMG could not build such a tree in any case:
``family.average_kinetics`` guards on a closed allowlist of
``[Arrhenius, SurfaceChargeTransfer, ArrheniusChargeTransfer, Marcus]`` and
``BadnellRRArrhenius`` is not on it, exactly as ``VoronovEIArrhenius`` is not.

COVERAGE: TWO ENTRIES, FROM TWO DIFFERENT SOURCES, FOR TWO DIFFERENT REASONS
-----------------------------------------------------------------------------
This library held exactly one entry (Li+, from ``badnell.yaml``) until I-234 added argon
(Ar+, transcribed from Shull & Van Steenberg 1982). The count is not the point; the
**provenance split** is, and it is why the walk below still matters. The first entry comes
from a shipped machine-readable table that RMG reads by ``(Z, N)``. The second cannot,
because that table does not reach argon, so its four coefficients are hand-transcribed from
a named row of a published table. Anything said below about what ``badnell.yaml`` can cover
constrains the FIRST route only. The second route is limited by what a human can source and
transcribe, which is a different bound entirely and is argued at the argon entry itself.

THE BADNELL ROUTE, AND WHY IT YIELDS ONLY ONE ENTRY
----------------------------------------------------
``input/kinetics/badnell.yaml`` holds 33 nuclear charges spanning Z = 1-54 and 318 ``(Z, N)``
stages. Only ``N = Z - 1`` - a singly charged cation capturing an electron to give the
neutral - is a stage this database can represent at all; the other 306 are multiply charged
ions, which is a separate representational problem. That leaves **12**: Z = 1-12
(H+, He+, Li+, Be+, B+, C+, N+, O+, F+, Ne+, Na+, Mg+).

Of those 12, RMG can construct both endpoints in their gas-phase ground states for **6**:
H, He, Li, N, O, Ne. (Be, B, Na and Mg have no RMG atom types - ``KeyError``; C+ as
``C u1 p1 c+1`` and F+ as ``F u2 p2 c+1`` fail ``AtomTypeError``.) Of those 6, exactly
**one** has thermochemistry for the reactant cation in this database as a free monatomic
ion: Li+ (``[Lip]``, ``LithiumPrimaryThermo`` index 65, ``computationalLithiumElectrode``).
H+ exists as ``proton`` in ``electrocatThermo`` / ``electrocatLiThermo``, but that is an
electrocatalysis reference species carrying the computational-hydrogen-electrode convention,
not a gas-phase proton.

So the Badnell route narrows 318 -> 12 -> 6 -> 1, and the one is Li+. Two consequences
worth naming:

* The bound is thermochemistry, not this table and not this owner. Adding He+, N+, O+ or Ne+
  needs monatomic-cation thermochemistry that does not exist here; that is a thermo ticket,
  and until it lands those reactions could not enter a model whichever owner was chosen.
* **Argon is not reachable by this route, and that is why the argon entry is transcribed
  by hand.** Ar is this campaign's benchmark bath gas and its electron-impact ionization *is*
  in ``voronov.yaml``, but ``badnell.yaml`` carries no ``Z = 18, N = 17`` stage - the table's
  cation-to-neutral stages stop at Z = 12. This paragraph used to end "an Ar-bath model can
  ionize argon and cannot radiatively recombine it", which was true of the database and was
  read as though it were true of the chemistry. I-234 closed it from the other direction: the
  rate exists in the literature, it is simply not in a table RMG parses, so it enters as four
  transcribed numbers with the row named. The limit was the ingest path, not the physics.

WHAT HAPPENS TO A SPECIES THIS LIBRARY DOES NOT COVER
-----------------------------------------------------
Nothing, and visibly. A library has no template, so an uncovered cation is never offered a
recombination reaction: no match, no tree descent, no averaged rule, no estimate. The
absence shows up as a missing channel, which a mechanism reader can see, rather than as a
wrong number, which they cannot.

USING IT
--------
Add ``'PlasmaRadiativeRecombination'`` to ``kineticsLibraries`` in the input file, supply the
electron species, and supply ``[Lip]`` and/or ``[Arp]`` - each entry is offered only if its
own cation is present. The reactor-facing form ``Li+ + e- => Li`` is produced
by ``rmgpy.electron_placement.resolve_electron_placement`` from the ``(1, 0)`` declaration;
the entry below is the canonical database form and must not be written with an explicit
electron participant, which the resolver refuses as double representation.
"""

entry(
    index = 0,
    label = "[Lip] => [Li]",
    degeneracy = 1,
    reversible = False,
    kinetics = BadnellRRArrhenius(Z=3, N=2),
    shortDesc = u"Li+ + e- => Li + hv",
    longDesc = u"""
Badnell (2006), Z=3, N=2: the Li II -> Li I radiative recombination stage. ``N`` is the
electron count *prior to* recombination, so N=2 is the two-electron ion Li+, per the
table's own ``notes`` field. Loaded from ``input/kinetics/badnell.yaml`` by ``(Z, N)``
rather than transcribed, so the shipped table stays the single source of the numbers and
no rate is authored here: A = 8.7e-12 cm^3/(molecule*s), B = 0.364, T0 = 147.0 K,
T1 = 7.153e6 K, C = 0.1508, T2 = 7.154e5 K.

``BadnellRRArrhenius`` supplies ``electrons = -1`` itself; ``KineticsLibrary.load``
propagates that onto the reaction, which is what lets ``Reaction.is_balanced`` close the
+1 -> 0 charge gap. Valid over Te = 10 K to 1e7 K per the class's own defaults - wider than
any condition an alkali plasma model is likely to reach, so unlike the Voronov ionization
entry this fit is never used outside its stated range.

Rate, measured against the pinned runtime (m^3/(mol*s), and cm^3/s per particle):

    Te = 0.3 eV (3481 K)   k = 3.392e5   alpha = 5.632e-13
    Te = 0.5 eV (5802 K)   k = 2.270e5   alpha = 3.770e-13
    Te = 1.0 eV (11605 K)  k = 1.301e5   alpha = 2.161e-13
    Te = 2.0 eV (23209 K)  k = 7.363e4   alpha = 1.223e-13

Physical inverse, named and NOT implemented here: **photoionization** Li + hv => Li+ + e-,
which is driven by a radiation field ``PlasmaReactor`` does not have. This reaction is NOT
the inverse of electron-impact ionization; that is three-body recombination
Li+ + 2 e- => Li + e-, a third-order channel with no shipped fit in this database.
""",
    reference = None,
    referenceType = "",
)

entry(
    index = 1,
    label = "[Arp] => [Ar]",
    degeneracy = 1,
    reversible = False,
    kinetics = TwoTemperaturePlasma(
        A = (3.77e-13, 'cm^3/(molecule*s)'),
        n = -0.651,
        Ea_g = (0.0, 'kJ/mol'),
        Ea_e = (0.0, 'kJ/mol'),
        T0 = (1e4, 'K'),
        electrons = -1,
        Tmin = (1e4, 'K'),
        Tmax = (1e8, 'K'),
    ),
    shortDesc = u"Ar+ + e- => Ar + hv  [Shull & Van Steenberg 1982, ApJS 48, 95, Table 2 row AR1]",
    longDesc = u"""
Radiative recombination of the argon cation to GROUND-STATE neutral argon. This is the
entry the ``PlasmaArgon`` library's longDesc says does not exist; that paragraph is now
stale and is corrected by the note at the end of this entry.

THE NUMBERS, AND WHERE EACH ONE IS TRANSCRIBED FROM
---------------------------------------------------
[ShullVanSteenberg1982]: J. M. Shull and M. Van Steenberg, "The Ionization Equilibrium of
Astrophysically Abundant Elements", Astrophys. J. Suppl. Ser. 48 (1982) 95-107.

Their equation (4) is the radiative-recombination fit

    alpha_r(T) = A_rad * (T / 10^4 K)^(-X_rad)      [cm^3/s]

and Table 2, row ``AR1`` (continued table, p. 99), carries for argon

    A_rad = 3.77E-13        X_rad = 6.51E-01

Both are transcribed verbatim from that row. ``A`` above is that A_rad written in the
paper's own units, so RMG performs the unit conversion and no arithmetic is done by hand;
``n = -0.651`` is ``-X_rad``, the sign flip being the difference between the paper's
``(T/10^4)^(-X_rad)`` and this class's ``(Te/T0)^n``; ``T0 = 1e4 K`` is the paper's own
normalisation. Nothing here is fitted, averaged or interpolated by this database.

WHICH ROW, AND WHY IT IS THE RIGHT ONE. Table 2's own footnote settles it:

    "Rates refer to collisional ionization of and recombination to the tabulated ion."

So the radiative coefficients on row ``X_n`` are recombination *to* stage ``X_n``, and row
``AR1`` is the reaction yielding neutral Ar I: Ar+ + e- => Ar. Two independent
corroborations, neither needed but both recorded: the last row of every element (C6, N7,
O8, NE10, MG12, SI14, S16) carries X_rad = 7.26E-01 with a null dielectronic entry, the
hydrogenic value, which only the bare nucleus recombining to the H-like ion can be; and
Verner's ``rrfit.f`` encoding of the same paper keys argon on the electron count AFTER
recombination, giving A = 3.770e-13, B = 0.6510 at IN = 18 (neutral argon, 18 electrons).

TEMPERATURE: THIS ENTRY READS Te, NOT THE GAS TEMPERATURE
----------------------------------------------------------
This is a two-temperature system and the distinction is load-bearing, so it is stated
plainly and it was verified rather than assumed.

``TwoTemperaturePlasma`` sets ``uses_electron_temperature = True`` and exposes
``get_rate_coefficient_two_temp(T, Te)``, which computes ``A * (Te/T0)^n`` - the electron
temperature, and only the electron temperature, drives this rate. With ``Ea_g = Ea_e = 0``
the class's Kossyi form collapses to exactly the paper's power law, so this is an exact
representation of equation (4) and not an approximation of it.

``PlasmaReactor`` routes it correctly: ``evaluate_two_temperature_rate_coefficient``
(``rmgpy/solver/plasma.pyx``) dispatches every ``uses_electron_temperature`` object to
that two-temperature evaluator, and its docstring records that the ordinary
``get_rate_coefficient(T)`` interface "is deliberately never used for these kinetics: it
collapses to a one-temperature evaluation (k(T, Te=T))."

Measured, at the 5 torr argon deck's conditions (Tgas = 298.15 K, Te = 34813.5 K = 3 eV):

    two-temperature evaluator   alpha = 1.674e-13 cm^3/s      <- what is used
    gas-temperature collapse    alpha = 3.711e-12 cm^3/s      <- 22.2x too high

So an entry that silently read the gas temperature here would be wrong by a factor of 22,
in the dangerous direction. It does not.

Rate, evaluated against the pinned runtime (m^3/(mol*s), and cm^3/s per particle):

    Te = 0.3 eV (3481 K)   k = 4.513e5   alpha = 7.493e-13
    Te = 0.5 eV (5802 K)   k = 3.236e5   alpha = 5.373e-13
    Te = 1.0 eV (11605 K)  k = 2.061e5   alpha = 3.422e-13
    Te = 2.0 eV (23209 K)  k = 1.312e5   alpha = 2.179e-13
    Te = 3.0 eV (34814 K)  k = 1.008e5   alpha = 1.674e-13
    Te = 5.0 eV (58023 K)  k = 7.228e4   alpha = 1.200e-13

VALIDITY RANGE - WHAT THE SOURCE STATES, AND WHAT IT DOES NOT
--------------------------------------------------------------
Read this before using the entry outside 1e4-1e8 K.

**Shull & Van Steenberg declare no numerical validity range for the fits themselves.**
They say only that they "attempted to simplify the rate coefficients with analytic fits
over the temperature range of interest" (Sec. II), without naming that range in Sec. II(b)
where the recombination fits are given.

``Tmin``/``Tmax`` above are therefore NOT a quoted bound and NOT an accuracy claim. They
are **grid membership, nothing more**: the span over which the authors themselves exercise
these rates, Table 3 tabulating argon ionization fractions at ``log T = 4.00`` through
``8.00`` in steps of 0.10, i.e. 1e4 K to 1e8 K. Sec. III adds that those results "are
applicable to any hot, optically thin, low density plasma in ionization equilibrium."
That the authors ran the fit over a span is evidence they considered it usable there; it
is not a demonstrated error bound, and it must not be read or cited as one. **No accuracy
bound for this fit is available from any source consulted.**

The deck this entry was measured on runs at Te = 34813.5 K, inside that span. The sibling
Li+ entry's ``BadnellRRArrhenius`` is valid down to 10 K, so the two entries in this
library do not share a floor.

**Nothing enforces these numbers, and that is measured, not assumed.** No evaluation path
consults them: ``is_temperature_valid(298.15)`` returns ``False`` while
``get_rate_coefficient_two_temp`` returns a perfectly ordinary number at Te = 0.5 eV
(5802 K, below ``Tmin``) with no warning and no raise. So ``Tmin``/``Tmax`` here are
documentation for a reader, not a guard against a caller. Pinned by
``test_the_declared_temperature_range_is_grid_membership_that_nothing_enforces``. Making
the engine enforce a declared range is an RMG-Py change and is referred, not attempted
here.

UNCERTAINTY - THERE IS NONE TO QUOTE, AND THAT IS THE STATEMENT
----------------------------------------------------------------
**Neither available source for this reaction states an uncertainty.** No error bar is
offered here, because none exists to offer. An absent quantity is reported absent.

What IS recorded below is a comparison between this fit and the one rival fit for the same
reaction. Read it as what it is - two particular calculations disagreeing - and not as an
uncertainty interval, a confidence bound, or a lower bound on the error. It supports none
of those readings: the two share an ancestor, so their agreement where they agree is
partly inherited rather than independent, and their disagreement where they disagree
measures the divergence of two parameterisations, not the distance of either from the
truth. An earlier draft of this entry advised a reader to use the spread as an error bar.
That advice was wrong and is withdrawn.

The rival fit is CHIANTI ``ar_2.rrparams`` - the six-parameter Badnell/Gu form
(A = 4.6460e-11 cm^3/s, B = 0.67040, T0 = 7.4230 K, T1 = 5.2750e6 K, C = 0.38320,
T2 = 3.9120e4 K), refitted for CHIANTI in 2008 by P. R. Young and K. P. Dere from
Aldrovandi & Pequignot, Rev. Bras. Fis. 4 (1974) 491; procedure documented in Dere et al.,
A&A 498 (2009) 915, Sec. 3. At the deck's working point:

    Shull & Van Steenberg 1982   alpha(3 eV) = 1.674e-13 cm^3/s
    CHIANTI ar_2 / AP74          alpha(3 eV) = 2.472e-13 cm^3/s
    spread                       ~48 %

The spread is strongly Te-dependent: the two fits agree to 1-3 % at 0.3-1 eV and diverge
above it (1.20x at 2 eV, 1.48x at 3 eV, 1.99x at 5 eV), because the Gu form's
``C*exp(-T2/Te)`` term flattens the high-Te falloff while this single power law keeps
falling. They disagree most at the conditions this deck runs at. That is worth knowing
when choosing between them, and it is still not an error bar.

Two further facts about the pair, recorded for the same reason:

* **The two fits are not independent at the root.** Both descend from Aldrovandi &
  Pequignot; SVS82's Sec. II(b) cites AP (1973, 1976) as its radiative source. This is
  precisely why their difference cannot be read as an uncertainty: common ancestry makes
  the comparison uninformative about the error of either against reality.
* **The authors of this entry's source flag argon's class as unchecked.** SVS82 Sec. II(b)
  states the radiative coefficients came from AP for C, N, O, Ne, Mg, Si and S, and then:
  "Values for Ar, Ca, and Ni are derived by interpolating along isosequences." Their
  conclusion asks for exactly the check argon still lacks - "Future experimental cross
  sections or theoretical calculations of these rates for elements with Z > 10 would be
  valuable in checking the validity of our isoelectronic extrapolations." Argon is Z = 18.
  This interpolation is the compilers' own, disclosed in their paper and quoted here; it is
  not an interpolation performed by this database, but a reader must know it is there.

WHAT THE PRODUCT IS: A TOTAL RATE DELIVERED ENTIRELY TO GROUND STATE - AN UPPER BOUND
--------------------------------------------------------------------------------------
**This entry overstates ground-state argon production by an unknown amount. Treat the
rate as an upper bound on that channel, not as the channel.**

``alpha_r`` in SVS82 is the TOTAL radiative recombination coefficient - the sum over
capture into the ground level and into all excited levels (AP's method: ground level by
the Milne relation from photoionisation cross sections, excited levels hydrogenic). The
product written here is ground-state Ar alone, so every excited-state capture the total
includes is delivered here as if it were a ground-state capture.

**Why that cannot be justified by a timescale argument.** An earlier draft of this entry
argued that radiative cascade to ground runs on nanoseconds, ~1e6 times faster than the
deck's 1e-3 s termination, and concluded the lumping was therefore correct. That argument
does not hold and is withdrawn. Whether an excited state can be eliminated is decided by
what competes with its decay - collisional quenching, stepwise re-ionisation out of the
excited level, and radiation trapping of the resonance lines, which at 5 torr lengthens
effective radiative lifetimes by orders of magnitude - not by whether its bare radiative
lifetime is shorter than the length of the simulation. Comparing against the run's
termination time answers a question nobody asked.

Argon's 4s ``3P2``/``3P0`` levels are metastable and make the point concrete: population
reaching them is held, not delivered. This database carries ``Ar(3P2)``
(``PlasmaExcitedNeutralThermo``, I-221) but no reaction reaches or leaves it, so the
branching cannot be represented here whatever its value.

**The branching fraction is not sourced.** Neither SVS82 nor the CHIANTI/AP74 fit resolves
final states; both publish a total. A state-resolved calculation for this ion does exist -
C. Y. Li, Y. Z. Qu, J. G. Wang, "State-selective radiative recombination cross sections of
argon ions", JQSRT 113 (2012) 1920, doi:10.1016/j.jqsrt.2012.05.005 - whose abstract
states it covers Ar+ and reports n-, (n,l)- and fine-structure-resolved results together
with Maxwellian rate coefficients and analytic fitting parameters. **It could not be
retrieved** (publisher returns HTTP 403), so none of its numbers have been seen, let alone
checked; it is named as the obvious next source rather than as evidence. Until something
resolves the final states, the size of the overstatement is unknown, and this entry says
so rather than bounding it.

WHY A LIBRARY ENTRY AND NOT A FAMILY RATE
------------------------------------------
Not a preference - the family cannot take this reaction. ``Plasma_Radiative_Recombination``
roots its template on ``1 *1 R u0 px c[0,+1,...]``, and Ar+ in its gas-phase ground state is
``1 Ar u1 p3 c+1`` (3s2 3p5, one unpaired electron). ``u1`` does not match ``u0``, so the
root REFUSES the argon cation; measured directly, not inferred. The family's
``GAIN_RADICAL`` recipe is also the wrong direction for argon, whose recombination takes
u1 -> u0. Tracked as I-236, together with the more dangerous half of that defect (the root
DOES match neutral Ar and would drive it toward an anion RMG cannot construct).

WHAT THIS ENTRY DOES TO THE 5 TORR ARGON MODEL - IT DEPENDS WHICH OBSERVABLE
-----------------------------------------------------------------------------
Measured, not argued, and it inverts the expectation this entry was added under - but
"not negligible" is only true of one observable, and the campaign cares about the other
one. Both numbers are below. Significant for heavy-species composition; negligible for
electron density.

Radiative recombination is a slow channel, and at the deck's INITIAL state it is utterly
negligible: with n_e = 1e16 m^-3 against n_Ar = 1.62e23 m^-3, the RR sink is 7.5e-11 of the
ionisation source and the RR timescale for one Ar+ ion is ~600 s against a 1e-3 s run. On
that arithmetic alone the entry looks inert. **That arithmetic answers the wrong question**,
because it is evaluated at a state the system leaves immediately.

At Te = 3 eV the deck ionises away from its seed: the heavy-species neutral fraction falls
from 1.0 to 0.17 by t ~ 1e-5 s, while the ion NUMBER DENSITY rises by a factor of 1.4e5
(the mixture's volume grows 117.6x over the run, so the rise in density is much smaller
than the rise in mole count). The RR sink scales as n_e * n_Ar+ while the ionisation source
scales as n_e * n_Ar, so the two swap places as the gas ionises. The end states differ:

    without this entry   Ar/(Ar+Ar+) -> ~0        (argon ionises until the neutral is gone)
    with this entry      Ar/(Ar+Ar+) ->  1.213e-3 (an ionisation/recombination balance)

**This entry is the only loss channel in the mechanism, so it alone sets the balance.**
Equating the two channels gives n_Ar/n_Ar+ = alpha/k_iz, and with k_iz = 1.3781e-10 cm^3/s
from the shipped ``PlasmaArgon`` cross-section table at this Te:

    predicted  alpha / k_iz             = 1.214459e-3
    measured   Ar/Ar+ ratio at 1e-3 s   = 1.214449e-3

AND WHAT IT DOES NOT DO: THE ELECTRON DENSITY BARELY MOVES
-----------------------------------------------------------
The same two committed profiles, end state, as deltas of (with - without)/without:

    electron amount   (moles)      -1213 ppm
    mixture volume    (m^3)        -1203 ppm
    ELECTRON DENSITY  (mol/m^3)      -10.3 ppm     <- what the campaign is chasing
    heavy neutral fraction Ar/(Ar+Ar+)   0 -> 1.213e-3

Removing electrons from a CONSTANT-PRESSURE two-temperature mixture shrinks the mixture
almost exactly as fast as it removes them, so the density hardly changes. The volume is
set by V = R((n_total - n_e)*Tgas + n_e*Te)/P, and with this deck ionised to completion at
Te/Tgas = 116.8 the electron gas carries 99.15% of that sum. Take away 1213 ppm of the
electrons and 1203 ppm of the volume goes with them; the quotient moves by the ~1/117
residue, 10.3 ppm. The effect is not an artefact of the two arms stopping at different
times: comparing both at the earlier arm's final time gives the same -10.3 ppm.

The volume cancels out of any RATIO of two heavy species, which is exactly why the neutral
fraction is free to move by three orders while the density does not. Same run, same
physics, two observables, two honest answers.

Consequence for the campaign, stated plainly: **this channel is not a candidate explanation
for the electron-density discrepancy**, and no volumetric sink of any order can be, for the
same reason (I-235's three-body channel included). Only a non-volumetric loss - wall/
ambipolar diffusion, which is absent from this mechanism - escapes the cancellation.

**What that agreement establishes, and what it does not.** It is an integration consistency
check: the solver was handed these two coefficients and reproduces the ratio the algebra
implies from them, which is what a correct integrator should do. It confirms that the
implementation does what the rate expressions say. It is NOT an independent validation of
the rate, and it is not evidence that either coefficient is right.

The channel is determinative HERE because the channels that would really dominate argon
loss at 5 torr are absent from this mechanism - ambipolar diffusion to the wall, and
dissociative recombination of Ar2+. Both are named as absent; neither is modelled, and what
either would do to this balance is not predicted here, because dissociative recombination
depends on dimer formation and abundance and wall loss depends on transport and geometry,
none of which this model contains. Treat the 1.2e-3 neutral fraction as a property of this
two-reaction mechanism, not as a statement about argon.

CORRECTION TO A SIBLING LIBRARY. ``PlasmaArgon``'s longDesc states that radiative
recombination of argon "is NOT here, and does not belong", on three supports from I-120.
All three have now moved. Argon cation thermochemistry exists (``PlasmaCationThermo``
``[Arp]``), so the reactant is constructible. ``TwoTemperaturePlasma`` has been admitted to
``_NET_ELECTRON_KINETICS_CLASSES``, so a power-law Te form can carry a net electron count.
And the third - that the channel does not matter at the campaign's working point - was
established at Te = 1 eV, below the Te ~ 1.33 eV runaway threshold I-120 itself identified;
this deck runs at 3 eV, above it, where the measurement above shows the channel is
decisive. That paragraph is stale and should be revised when ``PlasmaArgon`` is next
touched; it is not edited from here. See ``docs/argon-radiative-recombination/report.md``.
""",
    reference = None,
    referenceType = "",
)
