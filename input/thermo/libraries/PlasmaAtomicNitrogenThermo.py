#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaAtomicNitrogenThermo"
shortDesc = "Fixed-manifold ideal-monatomic N, N(2D), N(2P) thermo"
longDesc = """Load before general libraries. Separate fixed electronic manifolds, not an equilibrium electronic partition sum. Valid for the declared 298-600 K plasma gas envelope; fine-structure populations use statistical weights."""

entry(
    index = 1,
    label = 'N',
    molecule = """multiplicity 4
1 N u3 p1 c0
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5, 0, 0, 0, 0, 56104.89763306678, 4.193859706638204], Tmin=(298,"K"), Tmax=(600,"K"))],
                  Tmin=(298,"K"), Tmax=(600,"K"), Cp0=(20.78618,"J/(mol*K)"), CpInf=(20.78618,"J/(mol*K)")),
    shortDesc = "Fixed electronic manifold; NIST/CODATA anchor",
    longDesc = """Ground N: CODATA review H298=472.68 +/-0.40 kJ/mol and S298(1 bar)=153.301 +/-0.003 J/(mol*K), via NIST WebBook https://webbook.nist.gov/cgi/cbook.cgi?ID=C17778880&Mask=1. Cp=5R/2 for a fixed monatomic state. Convention: NIST ASD (doi:10.18434/T4W30F) energies weighted by 2J+1: D J=5/2,3/2 at 19224.464,19233.177 cm-1; P J=1/2,3/2 at 28838.920,28839.306 cm-1. This entry has centroid 0.0 cm-1 and degeneracy 4. Shift entropy by R ln(g/4). Do not add an equilibrium electronic partition sum across the separately resolved species. Fine-structure splitting/population uncertainty is not represented by the constant-Cp manifold convention. No extension beyond 600 K is validated.""",
)

entry(
    index = 2,
    label = 'N(2D)',
    molecule = """multiplicity 2
electronicstate 2D
1 N u1 p2 c0
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5, 0, 0, 0, 0, 83769.59489088578, 5.110150438512356], Tmin=(298,"K"), Tmax=(600,"K"))],
                  Tmin=(298,"K"), Tmax=(600,"K"), Cp0=(20.78618,"J/(mol*K)"), CpInf=(20.78618,"J/(mol*K)")),
    shortDesc = "Fixed electronic manifold; NIST/CODATA anchor",
    longDesc = """Ground N: CODATA review H298=472.68 +/-0.40 kJ/mol and S298(1 bar)=153.301 +/-0.003 J/(mol*K), via NIST WebBook https://webbook.nist.gov/cgi/cbook.cgi?ID=C17778880&Mask=1. Cp=5R/2 for a fixed monatomic state. Convention: NIST ASD (doi:10.18434/T4W30F) energies weighted by 2J+1: D J=5/2,3/2 at 19224.464,19233.177 cm-1; P J=1/2,3/2 at 28838.920,28839.306 cm-1. This entry has centroid 19227.9492 cm-1 and degeneracy 10. Shift entropy by R ln(g/4). Do not add an equilibrium electronic partition sum across the separately resolved species. Fine-structure splitting/population uncertainty is not represented by the constant-Cp manifold convention. No extension beyond 600 K is validated.""",
)

entry(
    index = 3,
    label = 'N(2P)',
    molecule = """multiplicity 2
electronicstate 2P
1 N u1 p2 c0
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5, 0, 0, 0, 0, 97597.9919715531, 4.5993248147463675], Tmin=(298,"K"), Tmax=(600,"K"))],
                  Tmin=(298,"K"), Tmax=(600,"K"), Cp0=(20.78618,"J/(mol*K)"), CpInf=(20.78618,"J/(mol*K)")),
    shortDesc = "Fixed electronic manifold; NIST/CODATA anchor",
    longDesc = """Ground N: CODATA review H298=472.68 +/-0.40 kJ/mol and S298(1 bar)=153.301 +/-0.003 J/(mol*K), via NIST WebBook https://webbook.nist.gov/cgi/cbook.cgi?ID=C17778880&Mask=1. Cp=5R/2 for a fixed monatomic state. Convention: NIST ASD (doi:10.18434/T4W30F) energies weighted by 2J+1: D J=5/2,3/2 at 19224.464,19233.177 cm-1; P J=1/2,3/2 at 28838.920,28839.306 cm-1. This entry has centroid 28839.177333333337 cm-1 and degeneracy 6. Shift entropy by R ln(g/4). Do not add an equilibrium electronic partition sum across the separately resolved species. Fine-structure splitting/population uncertainty is not represented by the constant-Cp manifold convention. No extension beyond 600 K is validated.""",
)
