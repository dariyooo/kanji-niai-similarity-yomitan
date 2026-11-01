# kanji-niai-similarity-yomitan

Visually similar kanji from the [niai](https://github.com/mrahhal/niai) project for Yomitan and DaLang.

Each kanji gets up to 20 similar kanji with their similarity score as a `similar` stat,
e.g. `["了","","","",[],{"similar":"了 (1.00)  亅 (0.95)  …"}]`.
It is meant to be installed alongside a kanji dictionary like KANJIDIC.

## Sources

niai ranks similar kanji by a structural-similarity score (0-1), its data (`kanjis.json`) is vendored in
`vendored_sources/niai/` (see its README for the exact version). The build takes the `Similar` kanji of each of
its 10,350 kanji, 6,351 of them have similar kanji and get an entry.

## Installation

Make sure [uv](https://github.com/astral-sh/uv) is installed on your system and run

``` bash
uv sync
```

## Usage

``` bash
uv run build.py
```

This creates the dictionary in `out/` (`kanji-niai-similarity-yomitan.zip`, `.index.json` and `.manifest.json`).
The uncompressed dictionary is kept in `tmp/kanji-niai-similarity-yomitan/` for inspection.

## Development

``` bash
uv run ruff check .          # lint
uv run ruff format .         # format
uv run pyright               # type check
uv run pytest                # tests
```

The repo follows the [DaLang dictionary repo standard](https://github.com/dariyooo/dalang-dict-utils/blob/main/docs/repo-standard.md),
update the shared setup with `uvx copier update --trust`.

## Release

Push a tag with today's date:

``` bash
git tag 2026-11-01 && git push origin 2026-11-01
```

The *Release* workflow runs the checks, builds the dictionary with the tag as revision and publishes it as the GitHub release of the tag.
To redo a release, push the tag again with `git tag -f 2026-11-01 && git push -f origin 2026-11-01`.
Installed dictionaries pick up new releases through "Check for updates".

## License

Similarity data from [niai](https://github.com/mrahhal/niai) by Mohammad Rahhal (MIT).
