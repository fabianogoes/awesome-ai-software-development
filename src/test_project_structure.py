import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


class ProjectStructureTests(unittest.TestCase):
    def test_claude_md_is_symlink_to_agents_md(self):
        claude_md = REPO_ROOT / "CLAUDE.md"

        self.assertTrue(claude_md.is_symlink())
        self.assertEqual("AGENTS.md", claude_md.readlink().as_posix())

    def test_commands_source_of_truth_rule_exists(self):
        rule_path = REPO_ROOT / ".agents" / "rules" / "commands-source-of-truth.md"

        self.assertTrue(rule_path.exists())
        content = rule_path.read_text(encoding="utf-8").lower()
        self.assertIn(".agents/commands/", content)
        self.assertIn(".claude/commands/", content)
        self.assertIn("source of truth", content)
        self.assertIn("compatibilidade", content)

    def test_canonical_commands_exist_in_agents_directory(self):
        commands_dir = REPO_ROOT / ".agents" / "commands"

        self.assertTrue((commands_dir / "rebuild.md").exists())
        self.assertTrue((commands_dir / "release-check.md").exists())
        self.assertTrue((commands_dir / "test.md").exists())

    def test_claude_commands_remain_available_for_compatibility(self):
        commands_dir = REPO_ROOT / ".claude" / "commands"

        self.assertTrue((commands_dir / "rebuild.md").exists())
        self.assertTrue((commands_dir / "release-check.md").exists())
        self.assertTrue((commands_dir / "test.md").exists())

    def test_claude_commands_are_minimal_wrappers(self):
        commands_dir = REPO_ROOT / ".claude" / "commands"

        for name in ("rebuild.md", "release-check.md", "test.md"):
            content = (commands_dir / name).read_text(encoding="utf-8").lower()
            self.assertIn("compatibilidade claude code", content)
            self.assertIn(".agents/commands/", content)
            self.assertNotIn("## passos", content)

    def test_public_docs_exist(self):
        self.assertTrue((REPO_ROOT / "docs" / "purpose.md").exists())
        self.assertTrue((REPO_ROOT / "docs" / "shared-resources.md").exists())


if __name__ == "__main__":
    unittest.main()
