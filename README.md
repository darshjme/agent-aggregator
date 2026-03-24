# agent-aggregator

**Multi-source data aggregation utilities for AI agents.**

When your agent makes 5 tool calls and gets back overlapping data, `agent-aggregator` handles the messy part: merging, deduplicating, grouping, and computing statistics — zero dependencies, pure Python ≥ 3.10.

---

## Install

```bash
pip install agent-aggregator
```

---

## Quick Example — Multi-Source Agent Data Aggregation

```python
from agent_aggregator import (
    merge_dicts, deep_merge, merge_lists,
    dedupe_dicts, group_by, sum_by, count_by,
    stats, percentile,
)

# --- 5 tool calls return overlapping results ---
github_data   = {"repo": "agent-aggregator", "stars": 120, "language": "Python"}
pypi_data     = {"repo": "agent-aggregator", "downloads": 4500, "language": "Python"}
sonar_data    = {"repo": "agent-aggregator", "coverage": 94.2, "issues": 3}
readme_data   = {"repo": "agent-aggregator", "license": "MIT"}
ci_data       = {"repo": "agent-aggregator", "stars": 125, "build": "passing"}

# 1. Merge all dicts — last write wins for conflicts
merged = merge_dicts(github_data, pypi_data, sonar_data, readme_data, ci_data, strategy="last")
print(merged)
# {'repo': 'agent-aggregator', 'stars': 125, 'language': 'Python',
#  'downloads': 4500, 'coverage': 94.2, 'issues': 3, 'license': 'MIT', 'build': 'passing'}

# 2. Deep-merge nested config from multiple sources
base_config   = {"model": "gpt-4", "params": {"temperature": 0.7, "max_tokens": 512}}
user_config   = {"params": {"temperature": 0.3, "top_p": 0.9}}
final_config  = deep_merge(base_config, user_config)
# {'model': 'gpt-4', 'params': {'temperature': 0.3, 'max_tokens': 512, 'top_p': 0.9}}

# 3. Combine + deduplicate results from multiple search APIs
results_a = [{"id": 1, "title": "Intro to agents"}, {"id": 2, "title": "RAG pipelines"}]
results_b = [{"id": 2, "title": "RAG pipelines"},   {"id": 3, "title": "Tool use"}]
unique_results = dedupe_dicts(merge_lists(results_a, results_b), fields=["id"])
# 3 unique items

# 4. Group agent logs by source, count calls per source
logs = [
    {"source": "github", "latency_ms": 120},
    {"source": "stripe", "latency_ms": 85},
    {"source": "github", "latency_ms": 200},
    {"source": "openai", "latency_ms": 430},
    {"source": "stripe", "latency_ms": 90},
]
call_counts   = count_by(logs, "source")
# {'github': 2, 'stripe': 2, 'openai': 1}

total_latency = sum_by(logs, "source", "latency_ms")
# {'github': 320.0, 'stripe': 175.0, 'openai': 430.0}

# 5. Statistical summary of latencies
latencies = [log["latency_ms"] for log in logs]
summary   = stats(latencies)
p95       = percentile(latencies, 95)
print(f"mean={summary['mean']:.0f}ms  p95={p95:.0f}ms  max={summary['max']}ms")
# mean=185ms  p95=398ms  max=430ms
```

---

## API Reference

### Merger

```python
from agent_aggregator import merge_dicts, merge_lists, deep_merge

# Merge dicts — strategies: "last" | "first" | "list" | "sum"
merge_dicts({"a": 1}, {"a": 2}, strategy="last")   # {"a": 2}
merge_dicts({"a": 1}, {"a": 2}, strategy="first")  # {"a": 1}
merge_dicts({"a": 1}, {"a": 2}, strategy="list")   # {"a": [1, 2]}
merge_dicts({"a": 1}, {"a": 2}, strategy="sum")    # {"a": 3}

# Merge lists with optional deduplication
merge_lists([1, 2], [2, 3], dedupe=True)            # [1, 2, 3]
merge_lists([{"id":1}, {"id":2}], [{"id":2}],
           dedupe=True, key=lambda x: x["id"])      # 2 items

# Recursive dict merge
deep_merge({"a": {"x": 1}}, {"a": {"y": 2}})       # {"a": {"x": 1, "y": 2}}
```

### Grouper

```python
from agent_aggregator import group_by, count_by, sum_by, first_by

items = [{"cat": "A", "val": 10}, {"cat": "B", "val": 5}, {"cat": "A", "val": 20}]

group_by(items, "cat")             # {"A": [..., ...], "B": [...]}
count_by(items, "cat")             # {"A": 2, "B": 1}
sum_by(items, "cat", "val")        # {"A": 30.0, "B": 5.0}
first_by(items, "cat")             # {"A": {"cat":"A","val":10}, "B": {...}}
```

### Deduplicator

```python
from agent_aggregator import dedupe, dedupe_dicts, find_duplicates

dedupe([1, 2, 2, 3])                                        # [1, 2, 3]
dedupe([{"id":1}, {"id":1}, {"id":2}], key=lambda x:x["id"]) # 2 items

dedupe_dicts([{"id":1,"v":"a"}, {"id":1,"v":"b"}], ["id"])  # 1 item
find_duplicates([1, 2, 2, 3, 3])                            # [2, 3]
```

### Aggregator

```python
from agent_aggregator import stats, percentile, moving_average

stats([1, 2, 3, 4, 5])
# {"min":1,"max":5,"mean":3.0,"median":3.0,"count":5,"sum":15.0}

percentile([1..100], 95)           # ~95th percentile via linear interpolation
moving_average([1,2,3,4,5], 3)     # [1.0, 1.5, 2.0, 3.0, 4.0]
```

---

## Why agent-aggregator?

| Problem | Without | With |
|---------|---------|------|
| Merge 5 tool-call results | Custom dict loop, breaks on None | `merge_dicts(*results)` |
| Deduplicate search results | Set + manual loop | `dedupe_dicts(results, ["id"])` |
| Group logs by source | defaultdict boilerplate | `group_by(logs, "source")` |
| p95 latency from samples | numpy required | `percentile(values, 95)` |
| Deep-merge configs | Recursive function per project | `deep_merge(base, override)` |

**Zero dependencies. Pure stdlib. Ships in seconds.**

---

## License

MIT © Darshankumar Joshi
