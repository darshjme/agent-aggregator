"""Aggregator — statistical aggregation using stdlib only (no external deps)."""

from __future__ import annotations
import statistics
from typing import Any


def stats(values: list[float]) -> dict[str, Any]:
    """Compute descriptive statistics for a list of numeric values.

    Returns:
        dict with keys: min, max, mean, median, count, sum
    """
    if not values:
        return {"min": None, "max": None, "mean": None, "median": None, "count": 0, "sum": 0.0}
    floats = [float(v) for v in values]
    return {
        "min": min(floats),
        "max": max(floats),
        "mean": statistics.mean(floats),
        "median": statistics.median(floats),
        "count": len(floats),
        "sum": sum(floats),
    }


def percentile(values: list[float], p: float) -> float:
    """Compute the p-th percentile of values (0 <= p <= 100).

    Uses linear interpolation (same as numpy's default method).
    """
    if not values:
        raise ValueError("Cannot compute percentile of empty list")
    if not (0.0 <= p <= 100.0):
        raise ValueError(f"p must be in [0, 100], got {p}")
    floats = sorted(float(v) for v in values)
    n = len(floats)
    if n == 1:
        return floats[0]
    # Linear interpolation
    idx = (p / 100.0) * (n - 1)
    lower = int(idx)
    upper = lower + 1
    if upper >= n:
        return floats[-1]
    frac = idx - lower
    return floats[lower] + frac * (floats[upper] - floats[lower])


def moving_average(values: list[float], window: int) -> list[float]:
    """Compute moving average with given window size.

    Returns a list of the same length as input:
    - Positions where window doesn't fit use available elements (expanding window).

    Args:
        values: Input numeric list.
        window: Window size (must be >= 1).
    """
    if window < 1:
        raise ValueError(f"window must be >= 1, got {window}")
    if not values:
        return []
    floats = [float(v) for v in values]
    result: list[float] = []
    for i in range(len(floats)):
        start = max(0, i - window + 1)
        chunk = floats[start: i + 1]
        result.append(sum(chunk) / len(chunk))
    return result
