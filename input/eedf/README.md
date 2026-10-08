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

Each entry records:

- the LoKI-B process label;
- the source file SHA-256 and block;
- the threshold and the class;
- for class A, the RMG reaction and whether it exists in `PlasmaArgon` today.

Two more lists cover the rest:

- `not_assembled` lists every source block that was not used, with the reason. Together with the
  channels, this accounts for all 256 blocks in the five source files.
- `class_a_gaps` lists the class-A reactions and species still missing from the mechanism.

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

The conventions are mandatory and verified, not commentary:

- each one is declared once under `declared_conventions`, with a statement and the exact `applies_to`
  list;
- it is listed on every entry it applies to;
- it is named in that assembled block's `I-341 conventions` comment.

The checker re-derives, for each entry, which conventions the step from source block to assembled
collision actually needs. It fails if a convention is missing, undeclared, renamed or listed where it
does not apply. It also fails on any difference that no convention licenses. No convention licenses a
change to a table or a threshold.

**Carry-forward rule.** These conventions are part of what the data mean. Every downstream artefact
built on this set must name each convention it inherits, with its statement or a reference to this
map. That covers EEDF or rate-coefficient tables, their manifests, and any report or figure that
quotes results from them. Above all, it covers `ELASTIC_REUSE_GROUND`, which is a convention and not
data for the excited state. A table manifest that drops a convention is not a faithful description
of the table.

The ground-state descriptors stay `->` as in the development file. Owner ruling C3 needs the 1s4/1s2
superelastic inverse, so this is flagged per entry (`superelastic_required`) rather than changed here.

### Sources and citations

Each is cited as the LXCat recommended format asks, together with the database's own reference.

| file | SHA-256 | citation |
|---|---|---|
| `Ar_LXCat.txt` | see YAML | IST-Lisbon database, www.lxcat.net, retrieved on September 23, 2022 (the copy shipped with LoKI-B). L.L. Alves, "The IST-Lisbon database on LXCat", J. Phys. Conf. Series 2014, 565, 1 (as the file header writes it). Data group: A. Yanguas-Gil, J. Cotrino and L.L. Alves, J. Phys. D: Appl. Phys. 38, 1588 (2005). |
| `BSR_Ar_excited.txt` | see YAML | BSR database, www.lxcat.net, retrieved on October 8, 2026. O. Zatsarinny, Comp. Phys. Commun. 174, 273 (2006). O. Zatsarinny and K. Bartschat, J. Phys. B 46, 112001 (2013). Data: O. Zatsarinny, Y. Wang and K. Bartschat, Phys. Rev. A 89, 022706 (2014). |
| `BSR_Ar_ground.txt` | see YAML | BSR database, www.lxcat.net, retrieved on October 8, 2026 (BSR-500). Comparison only, not assembled. |
| `NGFSRDW_Ar_excited.txt` | see YAML | NGFSRDW database, www.lxcat.net, retrieved on October 8, 2026. R.K. Gangwar, L. Sharma, R. Srivastava and A.D. Stauffer, J. Appl. Phys. 111, 053307 (2012). Comparison only, not assembled. |
| `TRINITI_Ar.txt` | see YAML | TRINITI database, www.lxcat.net, retrieved on October 8, 2026. The `Ar*` ionisation block cites "A.J. Dixon, J. Phys. B 9, 2617 (1976)" in a garbled comment; that attribution is not verified. |

The full hashes are in the YAML `sources` block.

### Checking the map

```
python scripts/check_eedf_channel_map.py input/eedf/argon_channel_map.yaml \
    --assembled <store>/assembled/ar-v1 \
    --sources <store>/incoming --sources <directory holding the IST-Lisbon Ar_LXCat.txt> \
    [--loki-rates <a LoKI-B rateCoefficients.txt solved on ar-v1>] [--database input]
```

`--sources` is required, because every entry is verified against the original source files. The
checker never relies on what the map or the assembled file says about itself. It prints
`RESULT: PASS` only when all of the following hold:

- the assembled files, read with LoKI-B's own grammar, contain nothing LoKI-B reads beyond the mapped
  blocks (see below);
- every collision LoKI-B would read from the assembled files is in the map exactly once, with the same
  file, threshold and reverse flag;
- for every entry, the source block re-derived from the hash-pinned source file has the cited block
  hash and starting line;
- the assembled collision's table and threshold equal that source block's;
- a block in a file copied byte for byte is that same block;
- every other difference is licensed by a declared convention, as described above;
- every reference to the same source block agrees;
- every source block is either mapped or listed in `not_assembled` exactly once, with the source's
  process string;
- every file hash matches;
- every entry has exactly one class in A/B/C/D, and every class-A entry carries an RMG mapping;
- the map is well formed, and every number in it is finite and compared with something independent:
  - thresholds with the source block;
  - ids, block numbers, lines and counts with the files;
  - RMG library indices with the library entry and its label (`--database`, by default this
    repository's `input`);
  - statistical weights with 2J+1 of the LS term;
  - `class_a_gaps` with the class-A entries that have no present reaction.

  The `power_share_max` values come from a solve the checker does not take as input, so it only
  requires them to be finite and in (0, 1].

A malformed map or block is refused with its location and a `RESULT: FAIL` line, never a traceback.

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

The checker runs that scan itself. It accepts only a canonical subset, on which the LXCat reading and
LoKI-B's cannot differ:

- every record LoKI-B reads must be the single parameter line, the descriptor and the five-dash table of
  exactly one collision block, and every block must be read exactly once;
- table rows must be two plain numbers, and the third line of a block must be a number;
- the descriptor must be in the one form the real data use, `[X + e -> Y + e, Type]`, with `<->` in
  place of `->` where the collision is reversible, one more `+ e` for Ionization, Type one of Elastic,
  Excitation or Ionization, and X and Y states that LoKI-B prints back unchanged. On this form, the label
  LoKI-B prints (`EedfCollisions.cpp` and `Gas.cpp` `operator<<`) is `e + X -> e + Y, Type`, or
  `e + X -> e + e + Y, Ionization`, written from the descriptor's own text. That is the label the map must carry, and it is checked without a
  rate list. LoKI-B also reads an electron written first or as `2e`, and drops it from the label;
  the checker refuses those forms rather than guess the label. The electron count must equal the source
  process's;
- the files must hold only printable ASCII, tab, LF and CRLF.

A table opened by a shorter dash line, a record without a keyword block, a `PARAM.:` in prose, a bare
CR, or a table ended by the end of the file is refused, even where LoKI-B would load it.

`scripts/test_eedf_channel_map_mutations.py` takes the same arguments. It applies 39 corruptions to
scratch copies outside the repository and expects the checker to refuse each one: exit 1 with
`RESULT: FAIL`, or an argparse usage error. A crash does not count as a refusal. The corruptions
include:

- swapped source references;
- an edited table, with the assembled-file hash refreshed to match;
- a wrong block hash hidden by reuse of the same block;
- a removed, renamed or narrowed convention;
- a dropped convention comment;
- an undeclared rename;
- a conflicting or overlapping `not_assembled` entry;
- a run without `--sources`;
- LoKI-B grammar edges: a two-dash shadow table ahead of the canonical one, a record without a keyword
  line, `PARAM.:` in header prose, a bare CR that hides a table row, a last table cut off before its
  closing line, and an ionisation descriptor missing an electron;
- printed labels: an electron written first on either side, and `2e`, each with the map label an
  earlier checker synthesised, run without `--loki-rates`;
- numbers and malformed input: a NaN or infinite map threshold, a NaN power share, a wrong
  statistical weight, a wrong RMG index, a dropped `class_a_gaps` id, a non-numeric third block line,
  and an entry with no `source`.

The unmodified map is the one case that must pass. The script exits 0 only when every case does what
it expects. Pass `--checker` to test another version of the checker.
