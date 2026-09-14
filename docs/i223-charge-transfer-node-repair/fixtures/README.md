# Fixtures for `check_family_generates.py`

Three minimal kinetics families, one training entry each, built so that the check has a positive
and a negative control for **each** of its two assertions without depending on any real family.

They exist because both defects the check catches were found in a real family that has since been
repaired — so the repaired family can only ever demonstrate the passing case. A check whose failing
case is unreachable is a check nobody can trust.

| fixture | generates? | own product raises? | the check should say |
|---|---|---|---|
| `Fixture_Healthy` | yes | no | `ok` |
| `Fixture_Inert_Recipe` | **no** | — | `INERT` |
| `Fixture_Own_Product_Raises` | yes | **yes** | `FAIL — 1 of its own products RAISE when fed back in` |
| `Fixture_Wrong_Products` | generates, but never the declared reaction | no | `FAIL — reproduces NONE of its own` |
| `Fixture_Unary_Product_Raises` | yes (**unary**) | **yes, only when fed back alone** | `FAIL — 1 of its own products RAISE` |

The last two were added in round 61, against two holes in the check rather than in a family:
it counted "returned a non-empty list" as generating, and it always handed the product-side
assertion **two** reactants, so a unary family was never tested at all.

All three carry the same one reaction, `O⁺ + N₂ → N₂⁺ + O`, and differ minimally:

- `Fixture_Healthy` is the reference. Its roots name the elements their subtrees use.
- `Fixture_Own_Product_Raises` changes exactly one line — **root A**, from `[H,O,metal]` to `R`.
  A group constrains atoms, not molecules, so `R … c[+1,…]` matches the formally-positive N of the
  family's own product N₂⁺. `GAIN_RADICAL` on it gives `N u2 p0 c0` holding a triple bond, which
  has no atom type, and `generate_reactions` raises.
- `Fixture_Inert_Recipe` changes the **recipe**, to `LOSE_CHARGE *1` + `GAIN_CHARGE *2`. Charge in
  RMG is derived, not stored — `apply_recipe` calls `update_charge()`, which recomputes it from a
  structure the charge actions never touched — so the products come back isomorphic to the
  reactants and `_create_reaction` discards them. Zero reactions, and the twelve standard family
  checks all pass on it.

  **It also has to revert both roots to `R`.** `generate_product_template` applies the recipe to
  the root **groups** at load time (`family.py:717` → `1077`), and with `[H,O,metal]` on root A
  `GroupAtom._lose_charge` raises `ActionError: Unknown atom type produced from set [H, O, metal]`.
  The rule is about **transitions, not element lists**: a charge action requires every atom type
  the root admits to have a charge transition available from it. A charge-only family whose roots
  name the six types that *do* carry one — `Li+ Na+ K+ Mg+ Ca+ Ar+` — loads fine and is just as
  inert. What survives is narrower and still useful: in *this* family the broad `R` root is what
  let the inert recipe hide, and an element-named root A would have surfaced it loudly at load
  time.

**The rate in each is a placeholder and is not a measurement.** `A = 1.0e-12 cm³/(molecule·s)`,
`n = 0`, `Ea = 0`. These families are test data; nothing here should ever be cited as chemistry.

## Running them

    python check_family_generates.py --selftest

which loads all three, asserts each produces its expected verdict, and fails loudly if any does
not. The same fixtures can be driven individually:

    python check_family_generates.py fixtures Fixture_Own_Product_Raises

## If you are the RMG-Py ticket picking this up

Copy this whole `fixtures/` directory next to the test that uses it. Nothing in it refers to
RMG-database, to the plasma campaign, or to any path outside itself. `check_family_generates.py`
has a section at the top of its docstring saying exactly where in `test/database/databaseTest.py`
the assertions belong and what they proved over the 103 installed families.
