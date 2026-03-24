"""Deduplicator — removes duplicates while preserving order."""

from __future__ import annotations
from typing import Any, Callable


def dedupe(items: list, key: Callable | None = None) -> list:
    """Remove duplicates from list, preserving first occurrence order.

    Args:
        items: Input list.
        key: Optional callable to extract the identity key. Defaults to the item itself.
    """
    seen: set = set()
    result: list = []
    for item in items:
        k = key(item) if key else item
        try:
            hash(k)
            hashable_k: Any = k
        except TypeError:
            # For unhashable types, use repr as fallback key
            hashable_k = repr(k)
        if hashable_k not in seen:
            seen.add(hashable_k)
            result.append(item)
    return result


def dedupe_dicts(items: list[dict], fields: list[str]) -> list[dict]:
    """Remove duplicate dicts based on specific fields, preserving order.

    Args:
        items: List of dicts.
        fields: Fields to use as composite identity key.
    """
    if not fields:
        raise ValueError("fields must be non-empty")
    seen: set = set()
    result: list[dict] = []
    for item in items:
        if not isinstance(item, dict):
            raise TypeError(f"Expected dict items, got {type(item).__name__}")
        composite = tuple(item.get(f) for f in fields)
        if composite not in seen:
            seen.add(composite)
            result.append(item)
    return result


def find_duplicates(items: list, key: Callable | None = None) -> list:
    """Return items that are duplicates (second+ occurrences).

    Args:
        items: Input list.
        key: Optional callable to extract identity key.
    """
    seen: set = set()
    duplicates: list = []
    for item in items:
        k = key(item) if key else item
        try:
            hash(k)
            hashable_k: Any = k
        except TypeError:
            hashable_k = repr(k)
        if hashable_k in seen:
            duplicates.append(item)
        else:
            seen.add(hashable_k)
    return duplicates
