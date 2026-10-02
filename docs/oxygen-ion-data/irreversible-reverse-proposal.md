# Engine proposal: preserve independent irreversible reverse channels

**Status: proposal only, not applied.** RMG-Py remains read-only. The strict
database regressions deliberately fail on the pinned runtime; no substitution,
xfail, or duplicate-flag workaround is accepted as channel preservation.

## Trace in the paired runtime

All line references are to `/home/alon/Code/RMG-Py-plasma/` as inspected for
this rework. The entry graphs and source coefficients need no change.

- `rmgpy/data/kinetics/library.py:474–480` constructs a normal LibraryReaction,
  retaining kinetics, duplicate and reversible fields. The container library
  is its family namespace. `rmgpy/rmg/model.py:1928–1936` passes library
  reactions to `make_new_reaction`; the seed route does the same at 1814–1823.
- `rmgpy/rmg/model.py:615–669` replaces participants with model species.
  At 681–684 it invokes `check_for_existing_reaction` and immediately returns
  the existing object if matched. A rejected new channel never reaches
  `register_reaction` at 703 or `new_reaction_list.append` at 753.
- Within one namespace, `rmgpy/rmg/model.py:545–559` checks identical forward
  IDs, honours duplicate handling, and restricts the reverse-ID branch to a
  **KineticsFamily**, not a KineticsLibrary. This permits the same-library
  argon excitation 87 and loss 89/91 to coexist. Their duplicate flags also
  satisfy the library-load validation; this is different from the model's
  cross-library existence check.
- At `rmgpy/rmg/model.py:580–588`, other KineticsLibrary namespaces are checked
  in either direction and a matching object is returned. A second reverse
  shortlist returns a match at 592–596. Neither site checks `reversible`,
  `duplicate`, or the kinetic law/carrier.
- `rmgpy/rmg/model.py:2446–2459` compares participants in either orientation,
  collider and per-side electron counts. It does not distinguish independently
  irreversible reverse channels or gas-temperature versus electron-impact
  rate laws. Opposite explicit electron placements in the focal pair match
  under that mirrored comparison.

Thus heavy 33 (`O + O- => O2 + e-`, ordinary gas-temperature Arrhenius) and
Air 55 (`O2 + e- => O- + O`, TwoTemperaturePlasma electron attachment) are
independent source channels but only the first offered object is retained.
All six library orders reproduce the loss. Setting the heavy entry's supported
`duplicate=True` in memory reproduces the same loss in all six orders.

No legitimate database-only metadata fix was found: the unconditional checks
ignore the relevant flags. Changing a participant graph or electron count
would change the reaction. Rewriting library authorship to impersonate Air,
adding fabricated provenance, or bypassing `check_existing` would conceal the
engine defect and is not an admissible source-data correction.

## Minimal proposed engine change

Change only the **cross-library** duplicate-check branches above. Retain the
existing participant/collider/electron test, but skip a candidate when both
reactions are irreversible and their actual participant lists are opposite.
For example, add a private predicate in `rmgpy/rmg/model.py`:

```python
def independent_irreversible_reverse(rxn, existing):
    return (not rxn.reversible and not existing.reversible
            and rxn.reactants == existing.products
            and rxn.products == existing.reactants)
```

At **both** cross-library match sites (currently lines 587 and 595), qualify
the existing condition:

```python
if (are_identical_species_references(rxn, rxn0)
        and not independent_irreversible_reverse(rxn, rxn0)):
    return True, rxn0
```

The lists are sorted by the checker before comparison. This is a scoped
proposal, not a change to the general species-reference predicate or family
deduplication. Same-direction cross-library duplicates still follow the
existing policy; a reverse match involving a reversible reaction still
deduplicates. Opposite irreversible channels proceed to normal registration,
retaining each original LibraryReaction, kinetics and provenance. No rate is
derived from equilibrium or merged with the other's rate law.

## Acceptance checks for the engine owner

Run the shipped database test module and `load_check.py` against the changed
runtime. In each of all six permutations of PlasmaArgon/PlasmaAir/PlasmaOxygenHeavy:

- One existing u1 doublet electron remains.
- Both heavy 33 and Air 55 are distinct admitted reactions in their own
  directions, with the exact entry/data references and independent rate laws.
- All four heavy detachment channels survive; Air 55 survives separately.
- Existing argon 87, 89 and 91 survive with their own kinetics.

Add engine-owned tests that a genuine same-direction duplicate still collapses,
a thermodynamic reverse involving a reversible reaction still collapses, and
either ordering of an independent irreversible reverse pair preserves both.
Repeat the whole-branch audit to verify every recorded opposite irreversible
pair survives in both orders. Finally rerun the full database Verifier and
require its failset to return to the reproduced base. The proposed change has
not been applied or tested as an engine fix in this task.
