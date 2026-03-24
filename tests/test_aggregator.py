"""Tests for aggregator module."""
import pytest
from agent_aggregator import stats, percentile, moving_average


def test_stats_basic():
    result = stats([1, 2, 3, 4, 5])
    assert result["min"] == 1.0
    assert result["max"] == 5.0
    assert result["mean"] == pytest.approx(3.0)
    assert result["median"] == pytest.approx(3.0)
    assert result["count"] == 5
    assert result["sum"] == pytest.approx(15.0)


def test_stats_single():
    result = stats([42.0])
    assert result["min"] == 42.0
    assert result["max"] == 42.0
    assert result["count"] == 1


def test_stats_empty():
    result = stats([])
    assert result["count"] == 0
    assert result["min"] is None
    assert result["mean"] is None


def test_stats_floats():
    result = stats([1.5, 2.5, 3.5])
    assert result["mean"] == pytest.approx(2.5)
    assert result["sum"] == pytest.approx(7.5)


def test_percentile_p50():
    values = list(range(1, 101))  # 1..100
    assert percentile(values, 50) == pytest.approx(50.5)


def test_percentile_p0():
    assert percentile([10, 20, 30], 0) == pytest.approx(10.0)


def test_percentile_p100():
    assert percentile([10, 20, 30], 100) == pytest.approx(30.0)


def test_percentile_p95():
    values = list(range(1, 101))
    result = percentile(values, 95)
    assert 94.0 < result < 100.0


def test_percentile_empty_raises():
    with pytest.raises(ValueError, match="empty"):
        percentile([], 50)


def test_percentile_out_of_range_raises():
    with pytest.raises(ValueError, match="p must be"):
        percentile([1, 2, 3], 101)


def test_percentile_single():
    assert percentile([7.0], 99) == 7.0


def test_moving_average_window_1():
    result = moving_average([1, 2, 3, 4, 5], window=1)
    assert result == pytest.approx([1, 2, 3, 4, 5])


def test_moving_average_window_3():
    result = moving_average([1, 2, 3, 4, 5], window=3)
    # [1], [1,2], [1,2,3], [2,3,4], [3,4,5]
    assert result == pytest.approx([1.0, 1.5, 2.0, 3.0, 4.0])


def test_moving_average_window_larger_than_list():
    result = moving_average([2, 4], window=10)
    assert result[0] == pytest.approx(2.0)
    assert result[1] == pytest.approx(3.0)


def test_moving_average_empty():
    assert moving_average([], window=3) == []


def test_moving_average_invalid_window():
    with pytest.raises(ValueError, match="window must be"):
        moving_average([1, 2, 3], window=0)
