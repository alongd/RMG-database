#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Double/groups"
shortDesc = u""
longDesc = u"""
Adsorption of a gas-phase triplet onto the surface. The unpaired electrons in the reactant form a double bond with the metal.

 *1         *1
     ---->  ||
~*2~       ~*2~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate", "VacantSite"], products=["Adsorbed"], ownReverse=False)

reverse = "Surface_Desorption_Double"

reactantNum=2
productNum=1

recipe(actions=[
    ['LOSE_RADICAL', '*1', 2],
    ['FORM_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*1', 1, '*2']
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
1 *1 R!H u2
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *2 Xv u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "C",
    group =
"""
1 *1 C u2
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "CH2",
    group =
"""
multiplicity [3]
1 *1 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CO",
    group =
"""
multiplicity [3]
1    O u0 p2 c0 {2,D}
2 *1 C u2 p0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "C2O",
    group =
"""
multiplicity [3]
1    O u0 p2 c0 {2,D}
2    C u0 p0 c0 {1,D} {3,D}
3 *1 C u2 p0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "N",
    group =
"""
1 *1 N u2
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "NH",
    group =
"""
multiplicity [3]
1 *1 N u2 p1 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "NN",
    group =
"""
multiplicity [3]
1    N u0 {2,S}
2 *1 N u2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "N2H2",
    group =
"""
multiplicity [3]
1    N u0 p1 c0 {2,S} {3,S} {4,S}
2 *1 N u2 p1 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "O",
    group =
"""
1 *1 O u2
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate
    L2: C
        L3: CH2
        L3: CO
        L3: C2O
    L2: N
        L3: NH
        L3: NN
            L4: N2H2
    L2: O


L1: VacantSite
"""
)


forbidden(
    label = "Ar_metastable_biradical",
    group =
"""
1 *1 Ar u2 p3 c0
""",
    shortDesc = """Metastable argon is out of scope for this family.""",
    longDesc = """
METASTABLE ARGON, Ar(4s 3P2), IS OUT OF SCOPE HERE AND ITS PRODUCTS ARE NOT
REPRESENTABLE.
`Ar u2 p3 c0` is metastable argon, entered in
input/thermo/libraries/PlasmaExcitedNeutralThermo.py. It is a BIRADICAL, and the atom
type that perceives it, Ar0e, is declared generic under R/R!H in RMG-Py
(rmgpy/molecule/atomtype.py) -- correctly, which is the point of this entry. Argon
brings 8 valence electrons, so in a MOLECULE 8 - c = bonds + 2p + u (the 8 is argon's
valence count, not a universal constant), and a bond-free neutral argon at p3 c0 has u2 and no
choice about it: Ar0e perceives exactly one molecule, this one. A generic site at
u2 is RIGHT to match it. What is missing is this family's own statement of scope,
which is what this entry supplies. This family is for adsorbing a gas-phase biradical onto two vacant surface sites, which is not chemistry a
noble gas participates in.

HOW THIS FAMILY WAS FOUND, AND WHY IT IS NOT A SIXTH GUESS. Not by trying partners. The
shipped template space was decomposed and every family whose per-reactant site admits
`Ar u2 p3 c0` was selected -- see docs/argon-metastable-thermo/template_space_derivation.py,
which re-runs and exits non-zero if any matching family lacks this entry. This family
matches on the forward template, slot 0. The earlier five entries were found by
running 140 families against a hardcoded partner list; that is exhaustive in families and
a SAMPLE in partners, and it missed this one because no suitable partner was in the list.

WHAT IT PREVENTS, MEASURED WITH A PARTNER DERIVED FROM THIS FAMILY'S OWN TEMPLATE
(docs/argon-metastable-thermo/template_witness_probe.py, so the witness does not depend on
anybody's choice of second reactant): Ar* + a vacant site, which raises while CONSTRUCTING Ar=X -- before any product exists.

WHY THE LABEL IS LOAD-BEARING. ForbiddenStructures.is_molecule_forbidden honours atom
labels (rmgpy/data/base.py), so an UNLABELLED `1 Ar u2 p3 c0` group silently matches
nothing during generation -- the molecule's argon is labelled *1 by then and cannot
map to an unlabelled group atom. This label is not chosen, it is read out of the
matcher's own mapping for this family's template.

THIS IS THE FIX, AT THE LAYER THE ERROR IS ON. Not a workaround held open pending an
engine change: the argon atom types are correct as they stand (owner's ruling,
2026-09-21; measured in docs/argon-metastable-thermo/atomtype_u_determined_probe.py).
atomtype.py's note that Ar0e "answers for five (u, p, c) triples" describes GROUP
patterns, where ux can be hand-written and no valency check applies -- families generate
molecules.

NOT COMPLETE, THOUGH -- but complete against the template space as it ships today. A
family added later whose site admits this structure would reopen the crash, and would be
declaring a u2 site broader than the chemistry it intends: the same defect as this one, in
that family, and fixed the same way. It would not be an engine defect returning. The
derivation above is the check that catches it, and it is re-runnable by whoever adds the
family.
""",
)
