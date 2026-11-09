"""CLI for repository release hygiene checks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from release_readiness.checker import check_project


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check common project release hygiene files.")
    parser.add_argument("directory", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--json", dest="json_path", type=Path, help="Write report to a JSON file")
    args = parser.parse_args(argv)

    try:
        report = check_project(args.directory)
        rendered = json.dumps(report, indent=2)
        print(rendered)
        if args.json_path:
            args.json_path.write_text(rendered + "\n", encoding="utf-8")
        return 0 if report["ready"] else 1
    except OSError as exc:
        print(f"release-readiness: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
