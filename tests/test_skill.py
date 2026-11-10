"""Public artifact checks only; these do not execute Rust or model evaluations."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/rust-architect/SKILL.md"
PROFILES = ("cli-tui", "backend", "library", "systems", "sources")


class SkillArtifactTests(unittest.TestCase):
    def core(self):
        return SKILL.read_text(encoding="utf-8")

    def test_metadata(self):
        text = self.core()
        front = text.split("---", 2)[1]
        for field in ('name: rust-architect', 'license: Apache-2.0',
                      'metadata:', '  author: "kozz36"', '  version: "1.0.0"'):
            self.assertIn(field, front)

    def test_description(self):
        lines = [line for line in self.core().splitlines() if line.startswith("description:")]
        self.assertEqual(len(lines), 1)
        match = re.fullmatch(r'description: "(Trigger: [^"\n]+)"', lines[0])
        self.assertIsNotNone(match)
        self.assertLessEqual(len(match[1]), 250)

    def test_section_order(self):
        self.assertEqual(re.findall(r"^## (.+)$", self.core(), re.M), [
            "Activation Contract", "Hard Rules", "Decision Gates",
            "Execution Steps", "Output Contract", "References"])

    def test_local_reference_paths(self):
        links = re.findall(r"\]\(([^)]+)\)", self.core())
        self.assertTrue(links)
        for link in links:
            self.assertNotRegex(link, r"^[a-zA-Z]+:|^/|#")
            target = (SKILL.parent / link).resolve()
            self.assertTrue(target.is_relative_to(ROOT.resolve()))
            self.assertTrue(target.is_file(), link)

    def test_required_profiles(self):
        for profile in PROFILES:
            path = SKILL.parent / "references" / (profile + ".md")
            self.assertTrue(path.is_file(), str(path))
            self.assertTrue(path.read_text(encoding="utf-8").strip())
            self.assertIn("references/" + profile + ".md", self.core())

    def test_source_ledger(self):
        text = (SKILL.parent / "references/sources.md").read_text(encoding="utf-8")
        urls = re.findall(r"https://[^\s|)]+", text)
        self.assertGreaterEqual(len(set(urls)), 12)
        self.assertLessEqual(len(set(urls)), 18)
        for line in text.splitlines():
            if "https://" in line:
                self.assertIn("2026-11-10", line)
        self.assertIn("1.99.1", text)
        self.assertIn("2026-10-15", text)
        self.assertIn("live", text.lower())

    def test_evaluation_schema(self):
        cases = json.loads((ROOT / "evaluations/cases.json").read_text(encoding="utf-8"))
        self.assertIsInstance(cases, list)
        self.assertEqual(len(cases), 12)
        self.assertEqual(len({case['id'] for case in cases}), 12)
        for case in cases:
            self.assertEqual(set(case), {"id", "prompt", "expected", "forbidden"})
            for field in ("id", "prompt"):
                self.assertIsInstance(case[field], str)
                self.assertTrue(case[field].strip())
            for field in ("expected", "forbidden"):
                self.assertIsInstance(case[field], list)
                self.assertTrue(case[field])
                self.assertTrue(all(isinstance(x, str) and x.strip() for x in case[field]))

    def test_readme_verification_and_scope(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v", text)
        self.assertIn("entire", text)
        self.assertIn("proposed", text.lower())
        self.assertIn("not executed", text.lower())

    def test_distribution_license(self):
        text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Apache License", text)
        self.assertIn("Version 2.0, January 2004", text)
        self.assertIn("END OF TERMS AND CONDITIONS", text)


if __name__ == "__main__":
    unittest.main()
