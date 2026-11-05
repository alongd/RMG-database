#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaNitrogenDissociativePooling"
shortDesc = "Optional N2(A) dissociative pooling model-transfer sensitivity"
longDesc = """
Optional high-pressure model transfer, not an evaluated low-pressure rate.
Include or omit this library to bracket dissociative pooling. The molecular
B/C branches in PlasmaNitrogenExcited remain unchanged. No electron energy
sink or thermal reverse is added. See README.md for the conditional sweep.
"""

entry(
    index = 1,
    label = "N2A + N2A => N2 + N + N",
    reversible = False,
    kinetics = Arrhenius(A=(120442835.8, "m^3/(mol*s)"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(600, "K")),
    shortDesc = "Optional high-pressure dissociative pooling transfer",
    longDesc = """
Jans et al. (2021), doi:10.1088/1361-6595/abcc7c.
Convention: transfer k_D=2e-16 m^3/(particle*s) from the high-pressure model
as an optional low-pressure sensitivity, not an evaluated low-pressure rate.
Apply to the lumped N2(A) manifold; N2 product is the ground-state lump.
The event rate is k_D*n_A^2 without an additional half. Each event consumes
two A molecules and produces two ground-state N atoms plus one N2 molecule.
Hold constant from 298 to 600 K as an unevaluated temperature extension.
Uncertainty: no measured low-pressure central value or statistical interval
is assigned. Compare runs with and without this library; conditional sweep
values 0, 2e-17, 1.73e-16, 2e-16 m^3/(particle*s) are illustrative sensitivities.
A_molar = k_particle * N_A; N_A=6.02214179e23 mol^-1.
""",
)
