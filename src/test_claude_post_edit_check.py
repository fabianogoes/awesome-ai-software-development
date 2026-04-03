import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parent.parent / "tools" / "scripts" / "claude_post_edit_check.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("claude_post_edit_check", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ClaudePostEditCheckTests(unittest.TestCase):
    def test_markdown_sources_trigger_rebuild(self):
        module = load_module()

        actions = module.determine_actions(["README.md"])

        self.assertEqual(
            [
                ("python3", "src/build.py"),
            ],
            actions,
        )

    def test_python_files_trigger_test_suite(self):
        module = load_module()

        actions = module.determine_actions(["src/build.py"])

        self.assertEqual(
            [
                ("python3", "-m", "unittest", "discover", "-s", "src", "-p", "test*.py", "-v"),
            ],
            actions,
        )

    def test_combined_changes_run_rebuild_then_tests(self):
        module = load_module()

        actions = module.determine_actions(["README.md", "tools/scripts/claude_post_edit_check.py"])

        self.assertEqual(
            [
                ("python3", "src/build.py"),
                ("python3", "-m", "unittest", "discover", "-s", "src", "-p", "test*.py", "-v"),
            ],
            actions,
        )

    def test_irrelevant_files_do_not_trigger_actions(self):
        module = load_module()

        actions = module.determine_actions(["docs/architecture.md"])

        self.assertEqual([], actions)


if __name__ == "__main__":
    unittest.main()
