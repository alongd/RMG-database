# Optional dissociative pooling

Use `PlasmaNitrogenDissociativePooling` together with the resolved atomic and
molecular nitrogen libraries. The single irreversible entry is
N2(A) + N2(A) -> N2(X) + 2 N(4S), with k_D = 2e-16 m^3/s.
This is a high-pressure model transfer from Jans et al. (2021),
doi:10.1088/1361-6595/abcc7c, **not an evaluated low-pressure rate**.
No measured low-pressure central value or numerical uncertainty interval is
claimed. The first production calculation must run with and without this
library. Existing B/C pooling branches are unchanged.

The coefficient is an event rate: R = k_D*n_A^2, with no extra factor one-half.
Gross A loss and atomic-N production are both 2R. The molar coefficient is
120442835.8 m^3/(mol*s), using N_A = 6.02214179e23 mol^-1. Transfer the rate
to the lumped A manifold and hold it constant over 298–600 K as explicit,
unevaluated conventions. The ground-state N2 product is lumped; no vibrational
partition, thermal reverse or additional electron-energy term is inferred.

## Conditional dependence on k_D

The following is the approved **conditional** planning sweep, reproduced from
its balance equations. It is not a physical power-balanced discharge or a
rigorous bound. It allocates the entire 0.5 W to A production at 6.17 eV/event
in a cylinder R=5 cm, L=30 cm at 5 Torr and 300 K. It assumes immediate
N(2P)->N(4S) recycling, omits electron dissociation and ions, and uses
**gamma_N = 1e-4**, the historical planning value. The declared production
central gamma is 5e-5, with the separate 1e-5–1e-3 bracket. Resolved excited
atoms in the actual model invalidate the immediate-recycling simplification.

Solve 2*k_D*n_A^2 = lambda_N*n_N + beta*n_N^2 and
q_A = lambda_A*n_A + (2.27e-16 + 2*k_D)*n_A^2 + 4.4e-17*n_N*n_A.
Here q_A = 0.5/(V*6.17*e), lambda_N = 0.731583 s^-1, and beta includes
both explicit Ar and N2 volume-recombination colliders. lambda_A includes the
argon-bath diffusion, 1/1.9 s^-1 radiation and the 3e-24*n_N2 quench bound.
The A-loss share by N is 4.4e-17*n_N divided by the complete bracketed A-loss
frequency above. These assumptions deliberately reproduce the earlier screen;
they are not the production physics.

| x_N2 | k_D (m3/s) | n_A (m^-3) | n_N (m^-3) | A-loss share by N |
|---|---:|---:|---:|---:|
| 0.01 | 0 | 9.55e+17 | 0 | 0 |
| 0.01 | 2e-17 | 4.12243e+17 | 9.15142e+18 | 0.773269 |
| 0.01 | 1.73e-16 | 2.10456e+17 | 2.02595e+19 | 0.873934 |
| 0.01 | 2e-16 | 2.00705e+17 | 2.12664e+19 | 0.874866 |
| 0.05 | 0 | 9.54958e+17 | 0 | 0 |
| 0.05 | 2e-17 | 4.12247e+17 | 9.15081e+18 | 0.773227 |
| 0.05 | 1.73e-16 | 2.10467e+17 | 2.02576e+19 | 0.873902 |
| 0.05 | 2e-16 | 2.00716e+17 | 2.12645e+19 | 0.874835 |
| 0.2 | 0 | 9.54802e+17 | 0 | 0 |
| 0.2 | 2e-17 | 4.12266e+17 | 9.14854e+18 | 0.773069 |
| 0.2 | 1.73e-16 | 2.10509e+17 | 2.02509e+19 | 0.873783 |
| 0.2 | 2e-16 | 2.00758e+17 | 2.12571e+19 | 0.874716 |

The zero-k_D row has zero atomic N only because this reduced sweep omits all
other N sources. The full mechanism also has electron-impact dissociation.
Physical N density, N-driven A-quenching share and k_D/gamma brackets at
x_N2 = 0.01, 0.05 and 0.2 remain to be calculated with the energy-balanced
engine and the qualified production EEDF table.
