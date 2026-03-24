# Changelog

All notable changes to `agent-aggregator` are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] — 2026-03-25

### Added
- **Merger**: `merge_dicts` with strategies (last/first/list/sum), `merge_lists` with deduplication, `deep_merge` for recursive dict merging
- **Grouper**: `group_by`, `count_by`, `sum_by`, `first_by` — all accepting callable or string keys
- **Deduplicator**: `dedupe`, `dedupe_dicts`, `find_duplicates` — all order-preserving
- **Aggregator**: `stats`, `percentile` (linear interpolation), `moving_average` (expanding window)
- Zero external dependencies — pure Python ≥ 3.10 stdlib only
- 59 pytest tests, 100% passing
- Full README with multi-source agent aggregation example
