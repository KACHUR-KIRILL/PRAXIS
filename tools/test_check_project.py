"""Regression checks using isolated copies; never mutate the working project."""

import contextlib
import io
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import check_project


class IntegrityTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="praxis-integrity-")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        source = check_project.ROOT
        shutil.copytree(
            source, self.root, dirs_exist_ok=True,
            ignore=shutil.ignore_patterns(".git", ".codex", ".venv", "__pycache__"),
        )
        self.addCleanup(patch.stopall)
        patch.object(check_project, "ROOT", self.root).start()

    def run_check(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = check_project.main()
        return code, output.getvalue()

    def test_current_project_passes(self):
        self.assertEqual(self.run_check()[0], 0)

    def test_missing_technical_carriers_fail(self):
        for name in (
            "tools/check_project.py", "tools/test_check_project.py", "tools/requirements.txt",
            ".github/workflows/project-integrity.yml",
            ".agents/skills/response-self-check/SKILL.md", ".agents/skills/project-brief/SKILL.md",
        ):
            with self.subTest(path=name):
                path = self.root / name
                original = path.read_bytes()
                path.unlink()
                try:
                    code, output = self.run_check()
                    self.assertEqual(code, 1)
                    self.assertIn(f"missing required carrier: {Path(name)}", output)
                finally:
                    path.write_bytes(original)

    def test_diverged_adapter_fails(self):
        (self.root / "CLAUDE.md").write_text("Changed adapter", encoding="utf-8")
        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("adapters must remain identical", output)

    def test_missing_concept_pointer_fails(self):
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8").replace(check_project.CURRENT_CONCEPT, "product/absent.md"),
                          encoding="utf-8")
        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("README does not point to current concept", output)

    def test_missing_link_target_fails(self):
        with (self.root / check_project.CURRENT_CONCEPT).open("a", encoding="utf-8") as stream:
            stream.write("\n[Missing](unavailable-artifact.md)\n")
        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("broken internal link", output)

    def test_local_codex_notes_are_ignored(self):
        path = self.root / ".codex/notes.md"
        path.parent.mkdir()
        path.write_text('[Scratch](absent.md)', encoding="utf-8")
        self.assertEqual(self.run_check()[0], 0)

    def test_code_examples_are_not_links(self):
        examples = (
            '```markdown\n[Example](absent.md)\n```\n',
            '~~~markdown\n[Example](absent.md)\n~~~\n',
            '    [Example](absent.md)\n',
            '`[Example](absent.md)`\n',
        )
        for content in examples:
            with self.subTest(content=content):
                (self.root / 'product/example.md').write_text(content, encoding='utf-8')
                self.assertEqual(self.run_check()[0], 0)

    def test_virtual_environment_is_not_project_content(self):
        path = self.root / '.venv/Lib/site-packages/example/README.md'
        path.parent.mkdir(parents=True)
        path.write_text('[Dependency documentation](not-shipped.md)', encoding='utf-8')
        self.assertEqual(self.run_check()[0], 0)

    def test_link_titles_and_encoded_paths(self):
        (self.root / 'product/my artifact.md').write_text('Artifact', encoding='utf-8')
        (self.root / 'product/example.md').write_text(
            '[Readme](../README.md "Project")\n'
            '[Artifact](my%20artifact.md)\n'
            '[Reference][artifact]\n\n[artifact]: <my artifact.md> "Title"\n',
            encoding='utf-8',
        )
        self.assertEqual(self.run_check()[0], 0)

    def test_missing_links_after_code_and_references_fail(self):
        for content in (
            '```\n[Example](absent-example.md)\n```\n\n[Real](absent.md "Title")',
            '[Real][ref]\n\n[ref]: absent.md "Title"\n',
            '![Image](absent.png "Title")',
        ):
            with self.subTest(content=content):
                (self.root / 'product/example.md').write_text(content, encoding='utf-8')
                code, output = self.run_check()
                self.assertEqual(code, 1)
                self.assertIn('broken internal link', output)
                self.assertNotIn('absent-example.md', output)

    def test_external_links_and_fragments_are_not_local_files(self):
        (self.root / 'product/example.md').write_text(
            '[Web](https://example.com/a) [CDN](//example.com/a) '
            '[Mail](mailto:test@example.com) [Section](#section)\n', encoding='utf-8',
        )
        self.assertEqual(self.run_check()[0], 0)

    def test_project_skill_links_are_still_checked(self):
        with (self.root / '.agents/skills/response-self-check/SKILL.md').open('a', encoding='utf-8') as stream:
            stream.write('\n[Missing](absent.md)\n')
        self.assertEqual(self.run_check()[0], 1)


if __name__ == "__main__":
    unittest.main()
