"""Tests for repository release hygiene checks."""

from pathlib import Path
import tempfile
import unittest

from release_readiness.checker import check_project


class ReleaseReadinessTests(unittest.TestCase):
    def test_complete_project_passes_all_checks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# Project", encoding="utf-8")
            (root / "LICENSE").write_text("MIT", encoding="utf-8")
            (root / "pyproject.toml").write_text("[project]", encoding="utf-8")
            (root / "tests").mkdir()
            (root / ".github" / "workflows").mkdir(parents=True)
            report = check_project(root)
        self.assertTrue(report["ready"])
        self.assertEqual(report["passed"], report["total"])

    def test_missing_items_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            report = check_project(directory)
        self.assertFalse(report["ready"])
        self.assertEqual(report["passed"], 0)
        self.assertEqual(report["total"], 5)

    def test_rejects_non_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "file.txt"
            file_path.write_text("x", encoding="utf-8")
            with self.assertRaises(NotADirectoryError):
                check_project(file_path)


if __name__ == "__main__":
    unittest.main()
