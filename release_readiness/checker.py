"""Evaluate a small set of repository release hygiene checks."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def check_project(root: str | Path) -> dict[str, Any]:
    """Return required-file checks for a project directory."""
    directory = Path(root)
    if not directory.is_dir():
        raise NotADirectoryError(f"not a directory: {directory}")

    readme = next(
        (name for name in ("README.md", "README.rst", "README.txt")
         if (directory / name).is_file()),
        None,
    )
    license_file = next(
        (name for name in ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING")
         if (directory / name).is_file()),
        None,
    )
    metadata_exists = (directory / "pyproject.toml").is_file()
    tests_exist = (directory / "tests").is_dir()
    workflows_exist = (directory / ".github" / "workflows").is_dir()

    checks = [
        {"name": "readme", "ok": readme is not None, "found": readme},
        {"name": "license", "ok": license_file is not None, "found": license_file},
        {"name": "python_project_metadata", "ok": metadata_exists,
         "found": "pyproject.toml" if metadata_exists else None},
        {"name": "tests_directory", "ok": tests_exist,
         "found": "tests/" if tests_exist else None},
        {"name": "github_actions_workflows", "ok": workflows_exist,
         "found": ".github/workflows/" if workflows_exist else None},
    ]
    passed = sum(1 for item in checks if item["ok"])
    return {
        "project": directory.name or str(directory),
        "passed": passed,
        "total": len(checks),
        "ready": passed == len(checks),
        "checks": checks,
    }
