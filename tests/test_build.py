from kanji_niai_similarity.build import INDEX_FIELDS, build_kanji_bank


def test_index_has_required_fields():
    for field in ("sourceLanguage", "author", "url", "description", "attribution"):
        assert field in INDEX_FIELDS


def test_kanji_bank_formats_similar_kanji_with_scores():
    entries = [{"Character": "了", "Similar": [{"Kanji": "了", "Score": 1.0}, {"Kanji": "亅", "Score": 0.954}]}]
    assert build_kanji_bank(entries) == [["了", "", "", "", [], {"similar": "了 (1.00)  亅 (0.95)"}]]


def test_kanji_bank_skips_kanji_without_similar_kanji_and_limits_them():
    entries = [
        {"Character": "一", "Similar": []},
        {"Character": "二", "Similar": None},
        {"Character": "口", "Similar": [{"Kanji": c, "Score": 0.5} for c in "日目田"]},
    ]
    assert build_kanji_bank(entries, max_similar=2) == [["口", "", "", "", [], {"similar": "日 (0.50)  目 (0.50)"}]]
