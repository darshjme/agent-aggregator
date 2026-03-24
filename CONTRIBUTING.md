# Contributing

Thank you for considering a contribution to `agent-aggregator`!

## Getting Started

```bash
git clone https://github.com/darshjme-codes/agent-aggregator
cd agent-aggregator
pip install -e ".[dev]"
```

## Running Tests

```bash
python -m pytest tests/ -v
```

All tests must pass before submitting a PR.

## Guidelines

- **Zero dependencies** — do not add external packages. Use Python stdlib only.
- **Order-preserving** — all deduplication and grouping functions must preserve insertion order.
- **Type hints** — all public functions must have complete type annotations.
- **Docstrings** — every public function needs a docstring explaining args and return value.
- **Tests** — every new function needs at least 3 tests: normal case, edge case (empty input), error case.

## Pull Request Process

1. Fork the repo and create a feature branch
2. Write your code and tests
3. Run `python -m pytest tests/ -v` — all must pass
4. Open a PR with a clear description of what changed and why

## Code Style

- Follow PEP 8
- Use `from __future__ import annotations` for forward refs
- Keep functions small and focused

## Reporting Bugs

Open a GitHub issue with:
- Python version
- Minimal reproducible example
- Expected vs actual output
