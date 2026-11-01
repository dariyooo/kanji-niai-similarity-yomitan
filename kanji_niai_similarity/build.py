"""Builds the niai visual similarity dictionary: the similar kanji of every kanji from the niai project."""

import json
from pathlib import Path

from dalang_dict import Vendored, build_index, fetch, package_dictionary

GITHUB_REPO = "dariyooo/kanji-niai-similarity-yomitan"
ASSET = "kanji-niai-similarity-yomitan"
TITLE = "Niai – Visual Similarity"

# `used_for` and the version are listed in the release notes
NIAI = Vendored(
    "kanjis.json",
    path="vendored_sources/niai/kanjis.json",
    version="4450292",
    used_for="similar kanji and their structural similarity scores (`Similar`)",
)
MAX_SIMILAR = 20

INDEX_FIELDS = {
    "sourceLanguage": "ja",
    "author": "mrahhal",
    "url": "https://github.com/mrahhal/niai",
    "description": "Kanji visual-similarity data from the niai project. "
    "Similar kanji are ranked by a structural-similarity score (0–1).",
    "attribution": "https://github.com/mrahhal/niai",
}


def load_niai_data(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array in {path}, got {type(data).__name__}")
    return data


def build_kanji_bank(entries: list[dict], max_similar: int = MAX_SIMILAR) -> list[list]:
    """One entry per kanji with similar kanji: [kanji, onyomi, kunyomi, tags, meanings, stats].

    Only the similarity stat is set, readings and meanings are left to dedicated kanji dictionaries.
    """
    bank = []
    for entry in entries:
        similar = (entry.get("Similar") or [])[:max_similar]
        if not similar:
            continue
        # Compact representation: "了 (1.00)  亅 (0.95)  …"
        stats = {"similar": "  ".join(f"{s['Kanji']} ({s['Score']:.2f})" for s in similar)}
        bank.append([entry["Character"], "", "", "", [], stats])
    return bank


def main() -> None:
    entries = load_niai_data(fetch(NIAI))
    print(f"Loaded {len(entries):,} kanji entries.")
    index = build_index(TITLE, GITHUB_REPO, ASSET, **INDEX_FIELDS)
    package_dictionary(ASSET, index, {"kanji_bank": build_kanji_bank(entries)})
