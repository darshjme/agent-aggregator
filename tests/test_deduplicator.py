"""Tests for deduplicator module."""
import pytest
from agent_aggregator import dedupe, dedupe_dicts, find_duplicates


def test_dedupe_basic():
    assert dedupe([1, 2, 2, 3, 1]) == [1, 2, 3]


def test_dedupe_preserves_order():
    result = dedupe([3, 1, 2, 1, 3])
    assert result == [3, 1, 2]


def test_dedupe_with_key():
    items = [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}, {"id": 1, "v": "c"}]
    result = dedupe(items, key=lambda x: x["id"])
    assert len(result) == 2
    assert result[0]["v"] == "a"  # first occurrence kept


def test_dedupe_empty():
    assert dedupe([]) == []


def test_dedupe_no_duplicates():
    assert dedupe([1, 2, 3]) == [1, 2, 3]


def test_dedupe_strings():
    assert dedupe(["a", "b", "a", "c"]) == ["a", "b", "c"]


def test_dedupe_dicts_single_field():
    items = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 1, "name": "Alice Duplicate"},
    ]
    result = dedupe_dicts(items, fields=["id"])
    assert len(result) == 2
    assert result[0]["name"] == "Alice"


def test_dedupe_dicts_composite_fields():
    items = [
        {"a": 1, "b": "x", "extra": 1},
        {"a": 1, "b": "y", "extra": 2},
        {"a": 1, "b": "x", "extra": 3},  # duplicate on (a, b)
    ]
    result = dedupe_dicts(items, fields=["a", "b"])
    assert len(result) == 2


def test_dedupe_dicts_empty_fields_raises():
    with pytest.raises(ValueError, match="fields must be non-empty"):
        dedupe_dicts([{"a": 1}], fields=[])


def test_dedupe_dicts_non_dict_raises():
    with pytest.raises(TypeError):
        dedupe_dicts([1, 2, 3], fields=["id"])


def test_find_duplicates_basic():
    dups = find_duplicates([1, 2, 2, 3, 3, 3])
    assert dups == [2, 3, 3]


def test_find_duplicates_none():
    assert find_duplicates([1, 2, 3]) == []


def test_find_duplicates_with_key():
    items = [{"id": 1}, {"id": 2}, {"id": 1}, {"id": 2}]
    dups = find_duplicates(items, key=lambda x: x["id"])
    assert len(dups) == 2
    assert all(d["id"] in (1, 2) for d in dups)


def test_find_duplicates_empty():
    assert find_duplicates([]) == []
