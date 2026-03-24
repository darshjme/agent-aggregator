"""Tests for grouper module."""
import pytest
from agent_aggregator import group_by, count_by, sum_by, first_by


ITEMS = [
    {"category": "api", "source": "github", "value": 10.0},
    {"category": "file", "source": "s3", "value": 5.0},
    {"category": "api", "source": "stripe", "value": 20.0},
    {"category": "db", "source": "postgres", "value": 7.5},
    {"category": "api", "source": "github", "value": 3.0},
]


def test_group_by_str_key():
    result = group_by(ITEMS, "category")
    assert set(result.keys()) == {"api", "file", "db"}
    assert len(result["api"]) == 3
    assert len(result["file"]) == 1


def test_group_by_callable_key():
    result = group_by(ITEMS, lambda x: x["source"])
    assert "github" in result
    assert len(result["github"]) == 2


def test_group_by_empty():
    assert group_by([], "category") == {}


def test_count_by_str_key():
    result = count_by(ITEMS, "category")
    assert result["api"] == 3
    assert result["file"] == 1
    assert result["db"] == 1


def test_count_by_callable():
    result = count_by(ITEMS, lambda x: x["source"])
    assert result["github"] == 2
    assert result["s3"] == 1


def test_sum_by_str_keys():
    result = sum_by(ITEMS, "category", "value")
    assert result["api"] == pytest.approx(33.0)
    assert result["file"] == pytest.approx(5.0)
    assert result["db"] == pytest.approx(7.5)


def test_sum_by_callable_keys():
    result = sum_by(ITEMS, lambda x: x["source"], lambda x: x["value"])
    assert result["github"] == pytest.approx(13.0)


def test_sum_by_non_numeric_raises():
    bad = [{"g": "a", "v": "not_a_number"}]
    with pytest.raises(TypeError):
        sum_by(bad, "g", "v")


def test_first_by_str_key():
    result = first_by(ITEMS, "category")
    assert result["api"]["source"] == "github"   # first api item
    assert result["file"]["source"] == "s3"


def test_first_by_callable():
    result = first_by(ITEMS, lambda x: x["source"])
    assert result["github"]["value"] == 10.0
