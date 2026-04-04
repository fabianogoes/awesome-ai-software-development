import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


class SetupScriptsTests(unittest.TestCase):
    def test_full_profile_template_files_exist(self):
        template_root = REPO_ROOT / "scripts" / "templates" / "full"

        self.assertTrue((template_root / "docs" / "decisions" / "0001-template.md").exists())
        self.assertTrue((template_root / "docs" / "runbooks" / "onboarding.md").exists())
        self.assertTrue((template_root / ".agents" / "agents" / "reviewer.md").exists())
        self.assertTrue((template_root / ".agents" / "rules" / "code-review.md").exists())

    def test_agents_template_file_exists(self):
        template_path = REPO_ROOT / "scripts" / "templates" / "common" / "AGENTS.md"

        self.assertTrue(template_path.exists())

    def test_shell_script_supports_full_profile(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.sh").read_text(encoding="utf-8")

        self.assertIn("full", content.lower())
        self.assertIn(".agents/agents/reviewer.md", content)
        self.assertIn(".agents/rules/code-review.md", content)
        self.assertIn("docs/decisions/0001-template.md", content)

    def test_shell_script_full_profile_templates_are_practical(self):
        content = (REPO_ROOT / "scripts" / "templates" / "full" / "docs" / "runbooks" / "onboarding.md").read_text(encoding="utf-8")
        adr_content = (REPO_ROOT / "scripts" / "templates" / "full" / "docs" / "decisions" / "0001-template.md").read_text(encoding="utf-8")
        reviewer_content = (REPO_ROOT / "scripts" / "templates" / "full" / ".agents" / "agents" / "reviewer.md").read_text(encoding="utf-8")
        rules_content = (REPO_ROOT / "scripts" / "templates" / "full" / ".agents" / "rules" / "code-review.md").read_text(encoding="utf-8")

        self.assertIn("Alternativas consideradas", adr_content)
        self.assertIn("Comandos principais", content)
        self.assertIn("python3 -m unittest", content)
        self.assertIn("Achados", reviewer_content)
        self.assertIn("Severidade", reviewer_content)
        self.assertIn("Severidade", rules_content)

    def test_shell_script_supports_standard_profile(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.sh").read_text(encoding="utf-8")

        self.assertIn("standard", content.lower())
        self.assertIn("docs/decisions", content)
        self.assertIn("docs/runbooks", content)
        self.assertIn("tools/scripts", content)
        self.assertIn("tools/prompts", content)
        self.assertIn("images", content)

    def test_shell_script_exposes_help_and_usage(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.sh").read_text(encoding="utf-8").lower()

        self.assertIn("usage", content)
        self.assertIn("--help", content)
        self.assertIn("minimal", content)
        self.assertIn("standard", content)
        self.assertIn("full", content)

    def test_shell_script_uses_external_templates_for_full_profile(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.sh").read_text(encoding="utf-8")

        self.assertIn("templates/full", content)

    def test_shell_script_uses_external_template_for_agents_md(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.sh").read_text(encoding="utf-8")

        self.assertIn("templates/common/AGENTS.md", content)

    def test_shell_script_does_not_create_clinerules(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.sh").read_text(encoding="utf-8")

        self.assertNotIn(".clinerules", content)

    def test_powershell_script_does_not_create_clinerules(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.ps1").read_text(encoding="utf-8")

        self.assertNotIn(".clinerules", content)

    def test_powershell_script_is_ascii_only_for_windows_powershell_compatibility(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.ps1").read_text(encoding="utf-8")

        try:
            content.encode("ascii")
        except UnicodeEncodeError as exc:
            self.fail(f"setup-agents.ps1 deve usar apenas ASCII: {exc}")

    def test_powershell_script_has_non_admin_fallback_for_links(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.ps1").read_text(encoding="utf-8")

        self.assertIn("Junction", content)
        self.assertIn("HardLink", content)

    def test_powershell_script_supports_standard_profile(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.ps1").read_text(encoding="utf-8")

        self.assertIn("standard", content.lower())
        self.assertIn("docs\\decisions", content)
        self.assertIn("docs\\runbooks", content)
        self.assertIn("tools\\scripts", content)
        self.assertIn("tools\\prompts", content)
        self.assertIn("images", content)

    def test_powershell_script_supports_full_profile(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.ps1").read_text(encoding="utf-8")

        self.assertIn("full", content.lower())
        self.assertIn(".agents\\agents\\reviewer.md", content)
        self.assertIn(".agents\\rules\\code-review.md", content)
        self.assertIn("docs\\decisions\\0001-template.md", content)

    def test_powershell_script_full_profile_templates_are_practical(self):
        content = (REPO_ROOT / "scripts" / "templates" / "full" / "docs" / "runbooks" / "onboarding.md").read_text(encoding="utf-8")
        adr_content = (REPO_ROOT / "scripts" / "templates" / "full" / "docs" / "decisions" / "0001-template.md").read_text(encoding="utf-8")
        reviewer_content = (REPO_ROOT / "scripts" / "templates" / "full" / ".agents" / "agents" / "reviewer.md").read_text(encoding="utf-8")
        rules_content = (REPO_ROOT / "scripts" / "templates" / "full" / ".agents" / "rules" / "code-review.md").read_text(encoding="utf-8")

        self.assertIn("Alternativas consideradas", adr_content)
        self.assertIn("Comandos principais", content)
        self.assertIn("python3 -m unittest", content)
        self.assertIn("Achados", reviewer_content)
        self.assertIn("Severidade", reviewer_content)
        self.assertIn("Severidade", rules_content)

    def test_powershell_script_exposes_help_and_usage(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.ps1").read_text(encoding="utf-8").lower()

        self.assertIn("usage", content)
        self.assertIn("-help", content)
        self.assertIn("minimal", content)
        self.assertIn("standard", content)
        self.assertIn("full", content)

    def test_powershell_script_uses_external_templates_for_full_profile(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.ps1").read_text(encoding="utf-8")

        self.assertIn("templates\\full", content)

    def test_powershell_script_uses_external_template_for_agents_md(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.ps1").read_text(encoding="utf-8")

        self.assertIn("templates\\common\\AGENTS.md", content)

    def test_windows_wrapper_uses_process_scoped_execution_policy_bypass(self):
        wrapper_path = REPO_ROOT / "scripts" / "setup-agents.cmd"

        self.assertTrue(wrapper_path.exists())

        content = wrapper_path.read_text(encoding="utf-8").lower()
        self.assertIn("powershell", content)
        self.assertIn("-executionpolicy bypass", content)
        self.assertIn("setup-agents.ps1", content)

    def test_windows_wrapper_passes_profile_argument(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.cmd").read_text(encoding="utf-8").lower()

        self.assertIn("%1", content)

    def test_windows_wrapper_supports_help_argument(self):
        content = (REPO_ROOT / "scripts" / "setup-agents.cmd").read_text(encoding="utf-8").lower()

        self.assertIn("--help", content)
        self.assertIn("-help", content)
        self.assertIn("full", content)

    def test_skill_mentions_agnostic_source_of_truth(self):
        content = (REPO_ROOT / "skills" / "claude-project-setup" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn(".agents/", content)
        self.assertIn("AGENTS.md", content)
        self.assertIn("fonte da verdade", content.lower())
        self.assertIn("minimal", content.lower())
        self.assertIn("standard", content.lower())
        self.assertIn("full", content.lower())


if __name__ == "__main__":
    unittest.main()
