"""Tests for merger module."""
import pytest
from agent_aggregator import merge_dicts, merge_lists, deep_merge


# --- merge_dicts ---

def test_merge_dicts_last_wins():
    a = {"x": 1, "y": 2}
    b = {"x": 99, "z": 3}
    result = merge_dicts(a, b, strategy="last")
    assert result == {"x": 99, "y": 2, "z": 3}


def test_merge_dicts_first_wins():
    a = {"x": 1}
    b = {"x": 99, "y": 2}
    result = merge_dicts(a, b, strategy="first")
    assert result == {"x": 1, "y": 2}


def test_merge_dicts_list_strategy():
    a = {"x": 1, "y": "hello"}
    b = {"x": 2, "z": 3}
    result = merge_dicts(a, b, strategy="list")
    assert result["x"] == [1, 2]
    assert result["y"] == ["hello"]
    assert result["z"] == [3]


def test_merge_dicts_sum_strategy():
    a = {"score": 10, "hits": 3}
    b = {"score": 5, "hits": 7, "errors": 1}
    result = merge_dicts(a, b, strategy="sum")
    assert result["score"] == 15
    assert result["hits"] == 10
    assert result["errors"] == 1


def test_merge_dicts_sum_non_numeric_fallback():
    a = {"name": "Alice"}
    b = {"name": "Bob"}
    result = merge_dicts(a, b, strategy="sum")
    assert result["name"] == "Bob"


def test_merge_dicts_empty():
    assert merge_dicts(strategy="last") == {}


def test_merge_dicts_single():
    assert merge_dicts({"a": 1}) == {"a": 1}


def test_merge_dicts_invalid_strategy():
    with pytest.raises(ValueError, match="Unknown strategy"):
        merge_dicts({"a": 1}, strategy="invalid")


def test_merge_dicts_type_error():
    with pytest.raises(TypeError):
        merge_dicts([1, 2, 3])


# --- merge_lists ---

def test_merge_lists_basic():
    assert merge_lists([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_merge_lists_dedupe():
    result = merge_lists([1, 2, 3], [2, 3, 4], dedupe=True)
    assert result == [1, 2, 3, 4]


def test_merge_lists_dedupe_with_key():
    a = [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}]
    b = [{"id": 2, "v": "c"}, {"id": 3, "v": "d"}]
    result = merge_lists(a, b, dedupe=True, key=lambda x: x["id"])
    ids = [item["id"] for item in result]
    assert ids == [1, 2, 3]


def test_merge_lists_no_dedupe_preserves_dups():
    result = merge_lists([1, 2], [2, 3])
    assert result == [1, 2, 2, 3]


def test_merge_lists_type_error():
    with pytest.raises(TypeError):
        merge_lists([1, 2], "not a list")


# --- deep_merge ---

def test_deep_merge_basic():
    base = {"a": 1, "b": {"c": 2, "d": 3}}
    override = {"b": {"c": 99}, "e": 5}
    result = deep_merge(base, override)
    assert result == {"a": 1, "b": {"c": 99, "d": 3}, "e": 5}


def test_deep_merge_override_wins_non_dict():
    base = {"a": {"x": 1}}
    override = {"a": "replaced"}
    result = deep_merge(base, override)
    assert result["a"] == "replaced"


def test_deep_merge_empty_override():
    base = {"a": 1}
    assert deep_merge(base, {}) == {"a": 1}


def test_deep_merge_nested_three_levels():
    base = {"a": {"b": {"c": 1}}}
    override = {"a": {"b": {"d": 2}}}
    result = deep_merge(base, override)
    assert result == {"a": {"b": {"c": 1, "d": 2}}}


def test_deep_merge_does_not_mutate_base():
    base = {"a": {"x": 1}}
    override = {"a": {"y": 2}}
    deep_merge(base, override)
    assert "y" not in base["a"]
