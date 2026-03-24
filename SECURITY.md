# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x     | ✅ Yes    |

## Reporting a Vulnerability

Please **do not** open a public GitHub issue for security vulnerabilities.

Email: darshjme@gmail.com

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

We aim to respond within 72 hours and patch within 14 days for confirmed issues.

## Scope

`agent-aggregator` is a pure-Python data processing library with zero external dependencies. It does not make network requests, read from disk, or execute arbitrary code. Attack surface is limited to malformed input data — always validate inputs from untrusted sources before passing to this library.
