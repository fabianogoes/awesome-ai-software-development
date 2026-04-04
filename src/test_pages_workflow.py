import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


class PagesWorkflowTests(unittest.TestCase):
    def test_pages_workflow_tracks_public_docs_and_tips(self):
        content = (REPO_ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")

        self.assertIn("CLAUDE_TIPS.md", content)
        self.assertIn("docs/purpose.md", content)
        self.assertIn("docs/shared-resources.md", content)

    def test_pages_workflow_does_not_publish_entire_repository_root(self):
        content = (REPO_ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")

        self.assertNotIn("path: '.'", content)
        self.assertIn("path: './dist'", content)
        self.assertIn("mkdir -p dist", content)
        self.assertIn("cp index.html dist/index.html", content)
        self.assertIn("cp -R images dist/images", content)


if __name__ == "__main__":
    unittest.main()
