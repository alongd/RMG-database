# `Plasma_Collisional_Ionization` — staged (not active)

These four files are the `Plasma_Collisional_Ionization` family carried from branch `99` and
translated to the target branch's electron convention per the rule in
[`../plasma_family_carry_translation_rule.md`](../plasma_family_carry_translation_rule.md). They are
**staged here under `docs/`, not installed under `input/kinetics/families/`**, so RMG does not load
them and the standing database suite stays green.

The family is held out of `input/` pending two decisions, both outside the carry ticket's scope and
both documented in the report above:

1. **`NO+` training species.** The two training entries (held as comments in `training/reactions.py`;
   `training/dictionary.txt` is empty) reference nitrosonium, whose `99` adjacency (`+1` on N, double
   bond) is chemically wrong and will not load on the target branch. The correct, loadable form is
   `N#[O+]` (charge on O, triple bond). Adopting it is a gated species-identity change.

2. **Spectator coverage gap.** With the electron translation applied the family loads through
   `groups`, but `kinetics_check_groups_nonidentical` then fails because the spectator
   `M = OR{N2,N,O2,O,Ar,He}` produces product-template clones `M1..M6` identical to the reactant
   groups — correct by construction for a third body, but a case the check was never written for.
   The fix is code-side (RMG-Py), not database.

To re-land once both are resolved: correct `NO+` to `N#[O+]` in `training/dictionary.txt`, re-enable
the two entries in `training/reactions.py`, and move this directory to
`input/kinetics/families/Plasma_Collisional_Ionization/`. `groups.py` (`electrons = 1`, `e-` stripped
from the template) and `rules.py` need no further change.
