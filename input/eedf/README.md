# Electron-collision channel maps for the LoKI-B electron kinetics

This directory holds frozen channel maps: one entry per electron collision that LoKI-B solves, each
with its class and, for class A, the RMG reaction it feeds. It holds **no cross-section data**.

- **A**: represented as an explicit RMG reaction and species transition.
- **B**: energy-only.
- **C**: diagnostic only, excluded from production.
- **D**: unsupported.

## The rule on data files

LXCat files and anything derived from them that carries cross-section values are **never committed to
this or any other repository, and never uploaded anywhere**. They live in a local LXCat store outside
version control. The maps carry only the following:

- each source file's name and SHA-256;
- the 1-based block number, starting line and per-block SHA-256 of every process used;
- thresholds, classes, conventions and RMG mappings.

If a store file does not hash to the value written here, the map does not describe it.

The two kinds of hash are computed differently:

- **File hashes** (`sha256`) are the SHA-256 of the file's raw bytes.
- **Block hashes** (`block_sha256`) are the SHA-256 of the block's UTF-8 text. A block runs from its
  collision-type keyword line (`ELASTIC`, `EFFECTIVE`, `EXCITATION`, `IONIZATION` or `ATTACHMENT`, alone
  on its line) through the second following line of five or more dashes. Before hashing, CRLF and CR line
  endings are converted to LF, and every line, including the last, ends with a single LF. The LXCat
  downloads use CRLF, so a hash of the raw byte slice gives a different digest.

## `argon_channel_map.yaml` (set `ar-v1`, I-341)

LoKI-B reads two files from the store:

- **`Ar_LXCat.txt`** is a byte copy of the IST-Lisbon argon file that the development tables use, shipped
  with LoKI-B. It holds 39 ground-state processes.
- **`Ar4s_assembled.txt`** holds 118 processes on the four 4s levels. They take the IST-Lisbon state names
  Ar(3P2) = 1s5, Ar(3P1) = 1s4, Ar(3P0) = 1s3 and Ar(1P1) = 1s2. Every table is copied unchanged from one
  named source block. The only additions are LoKI-B's `[lhs -> rhs, Type]` descriptor and a provenance comment.

### Generated, with one hand-written overlay

The map is **generated**. Three files make it:

- **`argon_channel_overlay.yaml`** is the only hand-written part: for each collision, keyed by the label
  LoKI-B prints, its class and, for class A, its RMG reaction; and, under `species`, for each species
  those reactions name (the electron included), the RMG dictionary record it stands for. Nothing else.
- **`scripts/gen_eedf_channel_map.py`** reads the local LXCat files, the overlay and the `PlasmaArgon`
  library, and writes the map. It derives everything else:
  - the collision-file inventory, from the assembled directory itself: every regular file with its
    SHA-256, and every file holding a `PARAM.:` line read as a collision file;
  - each collision's label, threshold and reverse flag, read with LoKI-B's own grammar, and its source
    block: the same block of a byte-identical source file, or the block its provenance comment names;
  - the conventions each collision needs, from the difference between source block and collision, and
    each convention's statement, written from the collisions it covers;
  - the state catalogue: 2J+1 weights, Paschen names from the order of the ground-state excitation
    thresholds, Racah names from the rename table;
  - source attribution, from each source file's own `DATABASE` and `PERMLINK` header lines;
  - every source block not assembled, with a reason derived from what the set uses and from the block's
    own table;
  - for class A, the library index, the status (`present`, `present_lumped`, `lumped_internal`,
    `absent`) and the missing species, from `PlasmaArgon`'s `reactions.py` and `dictionary.txt`, and
    the `class_a_gaps` list from those.
- **`scripts/check_eedf_channel_map.py`** reruns the generator and requires the committed map to equal
  its output **byte for byte**. No field of the map can be edited out of step with what it describes.

The generator refuses to write, and the checker fails, on any of the following:

- the assembled files, read as LoKI-B reads them, hold anything but the mapped blocks (see below);
- a collision's table or threshold differs from its hash-pinned source block, or the step from source to
  collision needs a change no convention licenses, or the assembled convention comment differs from the
  conventions the step needs;
- a 1s<->1s threshold differs by more than 0.01 eV from the gap between the two levels' ground-state
  excitation thresholds, so the state names do not match the source's levels;
- a source carries an elastic cross section for an excited target, which would make the
  `ELASTIC_REUSE_GROUND` statement false;
- the overlay misses a collision, names one LoKI-B does not read, or breaks the policy below;
- the overlay is not plain UTF-8 YAML: anchors, aliases, explicit tags, duplicate keys, non-string
  keys and strings that are not valid Unicode text are refused.

### The policy the overlay is held to

Each collision's family is derived from the source-verified process, not from the overlay:

| family | classes | class-A reaction |
|---|---|---|
| elastic | B | none |
| ionization | A | `<target species> + e- => <ion species> + e- + e-` |
| excitation into 4s (a load-bearing level, ruling C3) | A | `<target species> + e- => <product species> + e-`, `<=>` when the collision is `<->` |
| excitation above 4s | A or B, one class for the whole family | `<target species> + e- => Ar(1s_i) + e- + hv`, a radiative-cascade placeholder |

The above-4s families are ground->4p, ground->above 4p, 4s->4p and 4s->above 4p. Across the whole
overlay, each LoKI-B state maps to one RMG species. The overlay's reference record for that species must
be, as RMG reads it, one argon atom with the state's charge and, for an LS term, its spin multiplicity;
every species a reaction names, the electron included, must have one reference record, and no other
species may. Where `PlasmaArgon`'s dictionary holds the species, the record RMG loads must be the same
species as the reference by RMG's own comparison (`Species.is_isomorphic`, strict: the structure with
its electrons and charges, the multiplicity, and every state field RMG keeps, electronic state,
vibrational level, metal and facet); a record that differs is refused, naming the field. Each record,
reference and library alike, is also held to the LoKI-B state it stands for, so that a record copied
wrong into both, or the reference of a level the library lacks, is caught too: an electronic-state label
must be that state's LS term (`1S0` for the ground state, `3P2` for `Ars`, `1P1` for `Ar(1s2)`) and is
refused on a state with none (the ion), an argon atom or the electron has no vibrational level, metal or
facet, and the electron is a doublet; a field RMG leaves at its default says nothing. A reference
without a state field is an unresolved record, as the library's are. A 4s level the library lacks must
carry the canonical name `Ar(<Paschen name>)`, such as `Ar(1s4)`. A species that holds several 4s levels
stands for the lowest one; the others are `present_lumped` or `lumped_internal`.

### Declared conventions

These are conventions, not data:

- **`ELASTIC_REUSE_GROUND`**, by owner ruling 2026-10-08 ("(a) Literature, (b) meanwhile", option (b)). No
  LXCat set has an elastic momentum-transfer cross section for Ar(4s). LoKI-B refuses a populated state
  without one. Each Ar(1s) state therefore reuses the IST-Lisbon ground-state Ar elastic table unchanged.
- **`DETAILED_BALANCE_INVERSE`**: the 1s<->1s mixing processes are written `<->`. LoKI-B builds the downward
  process from the upward table by detailed balance, with g = 2J+1 (1s5 5, 1s4 3, 1s3 1, 1s2 3).
- **`LUMPED_TARGET_PER_LEVEL`**: TRINITI's single lumped `Ar*` ionisation table, with its threshold as
  given (4.2 eV), is applied to each of the four levels.
- **`STATE_RENAME`**: BSR's Racah names for the 4s levels become the IST-Lisbon term names, and TRINITI's
  ion `Ar(+)` becomes the IST-Lisbon ion state `Ar(+,gnd)`.

The generator derives which conventions each collision needs and writes each statement from the
collisions it covers. The assembled block's `I-341 conventions` comment must name the same set.

**Carry-forward rule.** These conventions are part of what the data mean. Every downstream artefact
built on this set must name each convention it inherits, with its statement or a reference to this
map. That covers EEDF or rate-coefficient tables, their manifests, and any report or figure that
quotes results from them. Above all, it covers `ELASTIC_REUSE_GROUND`, which is a convention and not
data for the excited state. A table manifest that drops a convention is not a faithful description
of the table.

The ground-state descriptors stay `->` as in the development file. Owner ruling C3 needs the 1s4/1s2
superelastic inverse, so this is flagged per entry (`superelastic_required`) rather than changed here.

The map does not carry electron-power shares. They are outputs of a LoKI-B solve, not something the
files determine; the I-341 run report holds them.

### Sources and citations

Each is cited as the LXCat recommended format asks, together with the database's own reference.

| file | SHA-256 | citation |
|---|---|---|
| `Ar_LXCat.txt` | see YAML | IST-Lisbon database, www.lxcat.net, retrieved on September 23, 2022 (the copy shipped with LoKI-B). L.L. Alves, "The IST-Lisbon database on LXCat", J. Phys. Conf. Series 2014, 565, 1 (as the file header writes it). Data group: A. Yanguas-Gil, J. Cotrino and L.L. Alves, J. Phys. D: Appl. Phys. 38, 1588 (2005). |
| `BSR_Ar_excited.txt` | see YAML | BSR database, www.lxcat.net, retrieved on October 8, 2026. O. Zatsarinny, Comp. Phys. Commun. 174, 273 (2006). O. Zatsarinny and K. Bartschat, J. Phys. B 46, 112001 (2013). Data: O. Zatsarinny, Y. Wang and K. Bartschat, Phys. Rev. A 89, 022706 (2014). |
| `BSR_Ar_ground.txt` | see YAML | BSR database, www.lxcat.net, retrieved on October 8, 2026 (BSR-500). Comparison only, not assembled. |
| `NGFSRDW_Ar_excited.txt` | see YAML | NGFSRDW database, www.lxcat.net, retrieved on October 8, 2026. R.K. Gangwar, L. Sharma, R. Srivastava and A.D. Stauffer, J. Appl. Phys. 111, 053307 (2012). Comparison only, not assembled; the sensitivity alternative for the 4s mixing (owner ruling 2026-10-14). |
| `TRINITI_Ar.txt` | see YAML | TRINITI database, www.lxcat.net, retrieved on October 8, 2026. The `Ar*` ionisation block cites "A.J. Dixon, J. Phys. B 9, 2617 (1976)" in a garbled comment; that attribution is not verified. |

The full hashes are in the YAML `sources` block.

### Regenerating and checking

```
python scripts/gen_eedf_channel_map.py --overlay input/eedf/argon_channel_overlay.yaml \
    --assembled <store>/assembled/ar-v1 \
    --source <the IST-Lisbon Ar_LXCat.txt shipped with LoKI-B> --source <store>/BSR_Ar_ground.txt \
    --source <store>/BSR_Ar_excited.txt --source <store>/NGFSRDW_Ar_excited.txt --source <store>/TRINITI_Ar.txt \
    --output input/eedf/argon_channel_map.yaml

python scripts/check_eedf_channel_map.py input/eedf/argon_channel_map.yaml \
    --overlay input/eedf/argon_channel_overlay.yaml --assembled <store>/assembled/ar-v1 --source ... \
    [--loki-rates <a LoKI-B rateCoefficients.txt solved on ar-v1>] [--database input]
```

Edit the overlay or the store, then regenerate; never edit the map. The checker prints `RESULT: PASS`
only when the derivation finds no problem and the map equals its output. With `--loki-rates`, LoKI-B's
own collision list must also be the derived one. A malformed map, overlay, store, source file or library file, a
directory that cannot be listed, and an `--output` that is a directory or cannot be written, is refused
with its reason and `RESULT: FAIL`, never a traceback.

The `--source` files must be exactly the ones the store's own `manifest.json` (in the assembled
directory) names, matched by SHA-256, in any order. The command line only says where each one is; its
manifest paths may be stale. Each source keeps the file name the manifest gives it, whatever name or
folder it is given from, and the sources read must be one-to-one with the manifest's. The collision
files in the assembled directory must be exactly the manifest's `loki_files`, with its hashes. The
manifest must also agree with itself: one file name and hash per source, and every source its process
and not-assembled records name among its sources. Then the generator derives the whole manifest from
the files and compares it with the declared one, field by field, naming each field that differs: `set`
and `ticket`; each source's file name, hash, `n_blocks` and `blocks_used`; the `statistical_weights`
and `paschen` catalogues; which `conventions` are used; and every field of every process (collision
file, LoKI-B label, descriptor, kind, target, product, direction, threshold, conventions, and its
source key, file, hash, block, line and block hash) and of every not-assembled record (source, block,
line, block hash, process). A process is known by its file and label and a not-assembled block by its
source and ordinal, so an omission, an extra or a duplicate is refused too, as is a field missing or
one the files do not give. Prose (`local_only`, the convention statements, the reasons) must be a
string but its words are not compared, and a path must name its file but may name any folder. Every
manifest field is also type-checked where it is read, so a malformed one is an input problem, and a
member name declared twice in one JSON object, at any depth, is refused with its field path: plain JSON
decoding keeps only the last, so the other declaration would never be compared. A source
or collision file left out, a file the manifest does not name, or a
manifest that is stale or contradicts itself is refused when generating and when checking.

The generator (and so the checker) reads each of `PlasmaArgon`'s two files, `reactions.py` and
`dictionary.txt`, exactly once, as bytes, and never opens them again: a file saved meanwhile is never
seen. RMG's own loader loads a private copy of those bytes, exactly as `KineticsDatabase.load_libraries`
loads a library (`KineticsLibrary(label=...).load(path, local_context, global_context)`), and whatever
RMG refuses is refused, with RMG's message: a species label or a multiplicity line written twice in
`dictionary.txt`, a malformed value in `reactions.py`, a non-UTF-8 file, a parameter given twice. Where
RMG's own error report fails while reporting (a `SyntaxError` in `reactions.py`), the error it was
handling is given as well. The reactions and species the map is derived from are then RMG's loaded
objects: the species dictionary RMG parsed while loading it, so a `//` comment is a comment, as RMG
reads it, and each reaction known by the dictionary species RMG resolved its reactants and products to
and by its direction, never by its label's text, so a label spelt another way (one space more) is the
same reaction. An entry that holds a mapped reaction's species another way (the other way round where
either is reversible, or with the other direction), or a mapped reaction held by several entries, cannot
be matched reliably and is refused, never reported absent, also when another entry holds it exactly. The
readers here parse the same bytes as a cross-check, and an entry index or label, or a species label,
they read otherwise than RMG loaded it is refused, naming it; their own refusals stand too (a form they
do not read, a dictionary label or multiplicity declared twice, a malformed literal). RMG-Py must
therefore be importable (on `PYTHONPATH`), and it must be one that can load the library: an RMG-Py
without the plasma kinetics (`ElectronCollisionPlasma`) refuses `PlasmaArgon`, and so does the checker.
RMG not importable is a refusal too, and so is an RMG-Py too old to keep a molecule's state fields
(electronic state, vibrational level), named with the fields it lacks; either refusal is reported alone,
before any record is read. RMG keeps whatever key an entry gives as its index, so an index that is not a
whole number (`None`, a string, a float) is refused as a `reactions.py` input error before anything
converts it.

The overlay is read with YAML's safe loader restricted to the scalar types its schema uses: a date or
time is not one, so an unquoted `2026-02-30` is the text it is written as, which the schema then
refuses, and a value the loader cannot construct is an overlay problem, never a traceback. A string
that is not valid Unicode text (a lone surrogate, which a YAML escape such as `"\uD800"` can write) is
refused where the overlay is read, and every diagnostic the generator and the checker print is escaped
to what standard output can hold.

`PlasmaArgon`'s `reactions.py` is read as RMG reads it (`rmgpy/util.py`: UTF-8 text, the
`RMG-PAIR-GENERATION` marker matched against `dictionary.txt` and removed), and that string is compiled
and parsed, not searched as text. A byte-order mark or a non-UTF-8 byte under another encoding cookie is
therefore refused, as RMG refuses it. An entry is read from each top-level `entry(...)` call with a
literal index and label, in any quoting or keyword order, and an entry kept inside a string or a comment
is not loaded, as in RMG. The file must compile, and each call must bind to RMG's
`KineticsLibrary.load_entry` parameters as Python binds them: a parameter given twice (by keyword, or by
position and keyword), an unknown parameter, or a missing index, label or kinetics is refused, as RMG
refuses it. Any other statement (a loop, a condition, a function, a computed index) is refused, because
only running the file would show what RMG loads.

`test/test_eedf_channel_map.py` checks, without the store, that the map is in the generator's exact
form, carries exactly the overlay, keeps its RMG fields in step with `PlasmaArgon`, that the library
reader loads what RMG's own `KineticsLibrary.load` loads (where `rmgpy` is importable), and that the
overlay loader, the policy, and the source and output handling refuse what they must. With the store named in `EEDF_LXCAT_ASSEMBLED` and
`EEDF_LXCAT_SOURCES`, it also regenerates the map and runs the checker and the mutation suite.

### How the assembled files are read

LoKI-B does not read the LXCat block layout. Its classic-file reader (add5518,
`EedfCollisions.cpp` `loadCollisionsClassic` and `LookupTable.cpp` `LookupTable::create`) works as follows:

- it splits lines at LF only;
- any line containing `PARAM.:`, anywhere in the file, starts a record;
- the next line must hold the `[lhs -> rhs, Type]` descriptor;
- the table opens at the first later line starting with two dashes;
- inside the table, lines starting with `#` are skipped;
- the table ends at the first line that does not start with two numbers, which must start with two
  dashes, or at the end of the file;
- every other line is ignored.

The generator runs that scan itself. It accepts only a canonical subset, on which the LXCat reading and
LoKI-B's cannot differ:

- every record LoKI-B reads must be the single parameter line, the descriptor and the five-dash table of
  exactly one collision block, and every block must be read exactly once;
- table rows must be two plain numbers, and the third line of a block must be a number;
- the descriptor must be in the one form the real data use, `[X + e -> Y + e, Type]`, with `<->` in
  place of `->` where the collision is reversible, one more `+ e` for Ionization, Type one of Elastic,
  Excitation or Ionization, and X and Y states that LoKI-B prints back unchanged. On this form, the label
  LoKI-B prints (`EedfCollisions.cpp` and `Gas.cpp` `operator<<`) is `e + X -> e + Y, Type`, or
  `e + X -> e + e + Y, Ionization`, written from the descriptor's own text. LoKI-B also reads an
  electron written first or as `2e`, and drops it from the label; the generator refuses those forms
  rather than guess the label. The electron count must equal the source process's;
- the files must hold only printable ASCII, tab, LF and CRLF.

A table opened by a shorter dash line, a record without a keyword block, a `PARAM.:` in prose, a bare
CR, or a table ended by the end of the file is refused, even where LoKI-B would load it.

### Mutation suite

`scripts/test_eedf_channel_map_mutations.py` takes the checker's arguments. It applies 202 mistakes to
scratch copies outside the repository and expects the checker to refuse each one for the reason the case
names: exit 1, `RESULT: FAIL` and a FAIL line holding that reason, or argparse's usage error. A crash,
or a traceback on stderr, does not count as a refusal. Ten controls must pass: the unmodified inputs,
the overlay rewritten in another layout, the library with one entry's label single-quoted or given
before its index or written with one space more, its dictionary's atoms labelled (`1 *1 Ar ...`), the
ground state labelled `electronicstate 1S0` in its record and its reference, the electron's record given
a lone pair or no charge (RMG normalises both on loading), and one source given from another folder
under another source's file name, which must also regenerate the committed map byte for byte. The
mistakes are every honest one the review rounds found:

- a hand edit to any field of the map: a hash, a block, a line, a threshold, a statement, a state name,
  a weight, a species list, a gap, an attribution, a non-finite number or key, a malformed value;
- a file left out of the store or the command line, when checking or when regenerating first, a source
  or collision file the store's manifest does not name, a manifest whose hash, file names or source
  records disagree, a stale or non-UTF-8 source file, an unreadable store directory;
- a library entry renumbered, disabled inside a string, put under a condition, or given its index,
  label or kinetics twice; a `reactions.py` saved with a byte-order mark or under a Latin-1 cookie, or
  holding a malformed value (a list as a dictionary key); a dictionary species or its multiplicity
  declared twice, the stale one first or last; a dictionary record behind a `//` comment, of the wrong
  spin or making a missing level present, or with an atom too many (Ar2 for an argon level); a mapped
  species given an electronic state, a vibrational level, a metal or a facet, or the electron without its
  unpaired electron, in its dictionary record, in its reference, or in both, including the reference of
  a level the library lacks; an entry 87 holds made reversible, or a reversible copy of it or of its
  reverse added beside it, or an exact copy; an entry's
  index that is no whole number (`None`, a word, an empty string, `"87"`); an overlay class or reaction
  written as an impossible date;
- a stale manifest: a process or not-assembled record missing, extra or duplicated, a process bound to
  another block or to none, a source's block count or used blocks out of date, a field of the wrong type;
  a statistical weight or Paschen name stale, missing or extra; a convention missing or extra; a stale
  set, ticket or path; a process's threshold, direction, descriptor, kind, target, product, conventions,
  source file, line or block hash stale; a not-assembled record's process or line stale; a field
  missing or extra; a member declared twice in the manifest's text, the stale value first or last;
  a library dictionary that is unreadable or not UTF-8;
- a table, name, comment or descriptor changed in the store, with the map's file hashes refreshed:
  LoKI-B grammar edges, swapped level names, a dropped convention comment;
- a mistyped overlay: an ionisation mapped to an excitation, a resonance level or an ionisation demoted,
  an elastic collision promoted, one above-4s collision moved out of its family's class, an unrelated or
  misnamed species, a singlet level lumped into a triplet species, a collision missing or extra, a
  duplicate key, an alias, a non-string key or class, invalid UTF-8, a lone surrogate in a key, a class
  or a reaction.

`--old-checker` runs the same cases against an earlier, map-only checker and prints both verdicts. The
suite's own inputs are checked before any case runs: a map or overlay that cannot be read or parsed (an
impossible date included), an overlay the generator refuses (`null`, `{}`, `[]`), a missing or
non-directory assembled path, a missing source, a `--checker` or `--old-checker` that is no file or
cannot be read, unmodified inputs the generator refuses, or a map whose bytes are not their
regeneration's (a CRLF copy included) is one `BAD  ...` line and exit 2, never a traceback and never a
run of the cases. The map and overlay are read once, and every case starts from those bytes, so a
fixture removed or saved again mid-run changes nothing.

### Written limits

Deliberate forgery by code run as the same user is outside what the checker can see. It does not catch:

1. **A change to the generator's own rules.** The generator and the checker are one program. Changing
   its policy table, its rename table, its convention statements or its reason rules, then regenerating,
   passes. Only review of the script's diff guards it.
2. **A replaced store file with a regenerated map.** The store is trusted through the hashes the
   committed map records. A source or assembled file replaced, or the store's `manifest.json` edited to
   name other sources, and the map regenerated and committed, passes; the new hash shows only in the
   diff. The checker cannot tell a re-download from a forgery.
3. **A decision within policy.** Moving a whole above-4s family between A and B, or lumping a 4s level
   into a library species of the right charge and multiplicity everywhere it appears, passes. These are
   owner decisions the checker cannot judge; they show as an overlay diff.
4. **What LoKI-B is told to load.** The consumer's setup file is not an input. The checker proves the
   assembled directory; `--loki-rates` proves one solve's collision list. The setup's statistical
   weights and populations are not checked against the map.
5. **The library is read, not loaded.** `reactions.py` is parsed, not run, so the generator knows which
   entries RMG loads and under which index and label, not whether RMG accepts each entry's kinetics or
   species; a library RMG refuses for another reason is not caught here (the database tests load it).
   The forms read are a strict subset: a few other libraries use forms outside it (an `entry(...),`
   expression, a float index), which would be refused, not misread.
   `dictionary.txt` is read with regular expressions; a dictionary in another layout reads as missing
   or wrong species, so the check fails rather than passes.
