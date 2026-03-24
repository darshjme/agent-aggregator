"""Merger — merges multiple dicts and lists from multiple agent tool calls."""

from __future__ import annotations
from typing import Any, Callable


def merge_dicts(*dicts: dict, strategy: str = "last") -> dict:
    """Merge multiple dicts using a given strategy.

    Strategies:
      - "last"  : last value wins (default)
      - "first" : first value wins
      - "list"  : collect all values into a list
      - "sum"   : sum numeric values; fall back to last for non-numeric
    """
    if strategy not in ("last", "first", "list", "sum"):
        raise ValueError(f"Unknown strategy '{strategy}'. Use: last, first, list, sum")

    result: dict[str, Any] = {}
    for d in dicts:
        if not isinstance(d, dict):
            raise TypeError(f"Expected dict, got {type(d).__name__}")
        for k, v in d.items():
            if k not in result:
                result[k] = [v] if strategy == "list" else v
            else:
                if strategy == "last":
                    result[k] = v
                elif strategy == "first":
                    pass  # keep existing
                elif strategy == "list":
                    result[k].append(v)
                elif strategy == "sum":
                    if isinstance(result[k], (int, float)) and isinstance(v, (int, float)):
                        result[k] = result[k] + v
                    else:
                        result[k] = v  # fallback: last wins for non-numeric
    return result


def merge_lists(*lists: list, dedupe: bool = False, key: Callable | None = None) -> list:
    """Merge multiple lists into one, with optional deduplication.

    Args:
        *lists: Lists to merge.
        dedupe: If True, remove duplicates while preserving order.
        key: Optional callable to extract identity key for deduplication.
    """
    merged: list = []
    for lst in lists:
        if not isinstance(lst, list):
            raise TypeError(f"Expected list, got {type(lst).__name__}")
        merged.extend(lst)

    if dedupe:
        seen: set = set()
        deduped: list = []
        for item in merged:
            k = key(item) if key else item
            try:
                hashable_k = k if not isinstance(k, dict) else id(k)
            except TypeError:
                hashable_k = id(item)
            if hashable_k not in seen:
                seen.add(hashable_k)
                deduped.append(item)
        return deduped

    return merged


def deep_merge(base: dict, override: dict) -> dict:
    """Recursively merge override into base. Override values take precedence.

    Dicts are merged recursively; all other types are replaced by override.
    """
    if not isinstance(base, dict):
        raise TypeError(f"Expected dict for base, got {type(base).__name__}")
    if not isinstance(override, dict):
        raise TypeError(f"Expected dict for override, got {type(override).__name__}")

    result = dict(base)
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result
