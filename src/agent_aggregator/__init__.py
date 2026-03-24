"""agent-aggregator: Multi-source data aggregation utilities for AI agents."""

from .merger import merge_dicts, merge_lists, deep_merge
from .grouper import group_by, count_by, sum_by, first_by
from .deduplicator import dedupe, dedupe_dicts, find_duplicates
from .aggregator import stats, percentile, moving_average

__version__ = "1.0.0"
__all__ = [
    "merge_dicts", "merge_lists", "deep_merge",
    "group_by", "count_by", "sum_by", "first_by",
    "dedupe", "dedupe_dicts", "find_duplicates",
    "stats", "percentile", "moving_average",
]
