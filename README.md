<div align="center">

<img src="assets/agent-aggregator-hero.png" alt="agent-aggregator — Vedic Arsenal by Darshankumar Joshi" width="100%" />

# ⚡ agent-aggregator

<h3><em>समाहार</em></h3>

> *Samahar — the gathering of distributed wisdom*

**Multi-source data aggregation for agents — Merger, Grouper, Deduplicator, Aggregator with stats/percentile. Zero dependencies.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://python.org)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen?style=flat-square)](https://github.com/darshjme/agent-aggregator)
[![Tests](https://img.shields.io/badge/Tests-Passing-success?style=flat-square)](https://github.com/darshjme/agent-aggregator/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Vedic Arsenal](https://img.shields.io/badge/Vedic%20Arsenal-100%20libs-purple?style=flat-square)](https://github.com/darshjme/arsenal)

*Part of the [**Vedic Arsenal**](https://github.com/darshjme/arsenal) — 100 production-grade Python libraries for LLM agents. Zero dependencies. Battle-tested.*

</div>

---

## Overview

`agent-aggregator` implements **multi-source data aggregation for agents — merger, grouper, deduplicator, aggregator with stats/percentile. zero dependencies.**

Inspired by the Vedic principle of *समाहार* (Samahar), this library brings the ancient wisdom of structured discipline to modern LLM agent engineering.

No external dependencies. Pure Python 3.8+. Drop it in anywhere.

## Installation

```bash
pip install agent-aggregator
```

Or clone directly:
```bash
git clone https://github.com/darshjme/agent-aggregator.git
cd agent-aggregator
pip install -e .
```

## How It Works

```mermaid
flowchart LR
    A[Input] --> B[agent-aggregator]
    B --> C{Process}
    C -- Success --> D[Output]
    C -- Error --> E[Handle / Retry]
    E --> B
    style B fill:#6b21a8,color:#fff
    note["Aggregator — Zero Dependencies"]
```

## Quick Start

```python
from aggregator import *

# Initialize
# See examples/ for full usage patterns
```

## Why `agent-aggregator`?

Production LLM systems fail in predictable ways. `agent-aggregator` solves the **aggregator** failure mode with:

- **Zero dependencies** — no version conflicts, no bloat
- **Battle-tested patterns** — extracted from real production systems
- **Type-safe** — full type hints, mypy-compatible
- **Minimal surface area** — one job, done well
- **Composable** — works with any LLM framework (LangChain, LlamaIndex, raw OpenAI, etc.)

## The Vedic Arsenal

`agent-aggregator` is part of **[darshjme/arsenal](https://github.com/darshjme/arsenal)** — a collection of 100 focused Python libraries for LLM agent infrastructure.

Each library solves exactly one problem. Together they form a complete stack.

```
pip install agent-aggregator  # this library
# Browse all 100: https://github.com/darshjme/arsenal
```

## Contributing

Found a bug? Have an improvement?

1. Fork the repo
2. Create a feature branch (`git checkout -b fix/your-fix`)
3. Add tests
4. Open a PR

All contributions welcome. Keep it zero-dependency.

## License

MIT — use freely, build freely.

---

<div align="center">

**Built with ⚡ by [Darshankumar Joshi](https://github.com/darshjme)** · [@thedarshanjoshi](https://twitter.com/thedarshanjoshi)

*"कर्मण्येवाधिकारस्ते मा फलेषु कदाचन"*
*Your right is to action alone, never to the fruits thereof.*

[Arsenal](https://github.com/darshjme/arsenal) · [GitHub](https://github.com/darshjme) · [Twitter](https://twitter.com/thedarshanjoshi)

</div>
