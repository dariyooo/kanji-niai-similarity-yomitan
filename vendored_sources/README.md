# Vendored sources

Frozen third-party data the dictionary is built from, one folder per source (`vendored_sources/{name}/`).

Every folder contains a `README.md` with:

* Origin: URL (and commit / version) the data was copied from
* License of the data
* Date it was retrieved

## niai

* Origin: [mrahhal/niai](https://github.com/mrahhal/niai) at commit `4450292` (2020-05-09), the last commit changing
  [`backend/src/Niai/data/kanjis.json`](https://github.com/mrahhal/niai/blob/main/backend/src/Niai/data/kanjis.json)
* `kanjiexp_judgements.yaml`: human similarity judgements of kanji pairs, kept for reference, not used by the build
* License: MIT (Mohammad Rahhal)
* Retrieved: 2026-03-15
