# Release Readiness Checker

A small, configurable-in-code Python CLI that checks whether a project contains a practical set of release hygiene files.

## Default checks

- A project README.
- A recognised license file.
- Python package metadata (`pyproject.toml`).
- A test directory.
- A GitHub Actions workflow directory.

The checker reports missing items as findings; it does not claim that the software is secure, defect-free, or ready for every organisation's release process.

## Requirements

- Python 3.10+
- No third-party runtime dependencies

## Usage

```bash
python -m release_readiness .
python -m release_readiness ./path/to/project --json readiness.json
```

Exit status is non-zero when required release hygiene items are missing, making the tool suitable for a local pre-release check or a CI step.

## Development

```bash
python -m unittest discover -s tests -v
```

## Scope

This is a lightweight repository-structure check. It does not run test suites, scan dependencies, validate licenses, or replace security and release approvals.

## License

MIT. See [LICENSE](LICENSE).
