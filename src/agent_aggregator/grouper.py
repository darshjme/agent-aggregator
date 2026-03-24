"""Grouper — groups and aggregates collections."""

from __future__ import annotations
from typing import Any, Callable


def _resolve_key(item: Any, key: Callable | str) -> Any:
    if callable(key):
        return key(item)
    if isinstance(key, str):
        if isinstance(item, dict):
            return item[key]
        return getattr(item, key)
    raise TypeError(f"key must be callable or str, got {type(key).__name__}")


def group_by(items: list, key: Callable | str) -> dict[str, list]:
    """Group items by key. Returns dict mapping key -> list of items."""
    result: dict[str, list] = {}
    for item in items:
        k = str(_resolve_key(item, key))
        result.setdefault(k, []).append(item)
    return result


def count_by(items: list, key: Callable | str) -> dict[str, int]:
    """Count items by key. Returns dict mapping key -> count."""
    result: dict[str, int] = {}
    for item in items:
        k = str(_resolve_key(item, key))
        result[k] = result.get(k, 0) + 1
    return result


def sum_by(
    items: list,
    group_key: Callable | str,
    value_key: Callable | str,
) -> dict[str, float]:
    """Sum values by group key. Returns dict mapping group_key -> sum of value_key."""
    result: dict[str, float] = {}
    for item in items:
        gk = str(_resolve_key(item, group_key))
        v = _resolve_key(item, value_key)
        try:
            v = float(v)
        except (TypeError, ValueError) as exc:
            raise TypeError(
                f"value_key must resolve to numeric, got {type(v).__name__}: {v!r}"
            ) from exc
        result[gk] = result.get(gk, 0.0) + v
    return result


def first_by(items: list, key: Callable | str) -> dict[str, Any]:
    """Return the first item per group key. Returns dict mapping key -> first item."""
    result: dict[str, Any] = {}
    for item in items:
        k = str(_resolve_key(item, key))
        if k not in result:
            result[k] = item
    return result
