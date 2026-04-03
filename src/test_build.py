import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from src import build


class BuildParsingTests(unittest.TestCase):
    def test_process_tools_uses_avaliacao_column(self):
        rows = [
            {
                "Ferramenta": "Codex",
                "Descrição": "Ferramenta de coding da OpenAI",
                "Link": "https://openai.com/codex",
                "Avaliação": ":star::star::star:",
            }
        ]

        html = build.process_tools(rows)

        self.assertIn("Recomendado", html)
        self.assertIn("rating-dot filled", html)

    def test_mcp_section_is_parsed_from_readme(self):
        readme = """
## Ferramentas

### MCP

| MCP | Descrição | Link | Avaliação |
| --- | --------- | ---- | --------- |
| Playwright MCP | Browser automation | https://github.com/microsoft/playwright-mcp | :hourglass: |
"""

        mcp_rows = build.parse_table(build.find_section(readme, "### MCP"))

        self.assertEqual(1, len(mcp_rows))
        self.assertEqual("Playwright MCP", mcp_rows[0]["MCP"])

    def test_plugins_section_is_parsed_from_readme(self):
        readme = """
## Ferramentas

### MCP

| MCP | Descrição | Link | Avaliação |
| --- | --------- | ---- | --------- |
| Playwright MCP | Browser automation | https://github.com/microsoft/playwright-mcp | :hourglass: |

### Plugins

| Plugin | Descrição | Link | Avaliação |
| ------ | --------- | ---- | --------- |
| Codex for Claude Code | Plugin da OpenAI | https://github.com/openai/codex-plugin-cc | :hourglass: |
"""

        plugin_rows = build.parse_table(build.find_section(readme, "### Plugins"))

        self.assertEqual(1, len(plugin_rows))
        self.assertEqual("Codex for Claude Code", plugin_rows[0]["Plugin"])

    def test_main_includes_plugins_in_generated_output_and_stats(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            (base / "README.md").write_text(
                """
## Ferramentas

### CLI

| Ferramenta | Descrição | Link | Avaliação |
| ---------- | --------- | ---- | --------- |
| Codex | CLI | https://openai.com/codex | :star::star::star: |

### IDE

| Ferramenta | Descrição | Link | Avaliação |
| ---------- | --------- | ---- | --------- |
| Cursor | IDE | https://cursor.com | :hourglass: |

### Frameworks

| Ferramenta | Descrição | Link | Avaliação |
| ---------- | --------- | ---- | --------- |
| Superpowers | Framework | https://github.com/obra/superpowers | :star: |

### MCP

| MCP | Descrição | Link | Avaliação |
| --- | --------- | ---- | --------- |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | :hourglass: |

### Plugins

| Plugin | Descrição | Link | Avaliação |
| ------ | --------- | ---- | --------- |
| Codex for Claude Code | Plugin | https://github.com/openai/codex-plugin-cc | :hourglass: |

### Skills

| Skill | Descrição | Link | Avaliação |
| ----- | --------- | ---- | --------- |
| Napkin | Skill | https://github.com/blader/napkin | :star: |

### Write

| Post | Link |
| ---- | ---- |
| Artigo | https://example.com/article |

### Video

| Post | Link |
| ---- | ---- |
| Video | https://example.com/video |

## Utilitários

| Ferramenta | Descrição | Link |
| ---------- | --------- | ---- |
| ADR | Template | https://example.com/adr |

## Cursos

- [Curso](https://example.com/course)
""".strip(),
                encoding="utf-8",
            )
            (base / "CONCEPTS.md").write_text("### RAG\nDescricao", encoding="utf-8")
            (base / "BOOKS.md").write_text(
                "| Livro | Autor | Link |\n| ----- | ----- | ---- |\n| Book | Author | https://example.com/book |",
                encoding="utf-8",
            )

            stdout = io.StringIO()
            with patch.object(build, "__file__", str(base / "src" / "build.py")):
                with redirect_stdout(stdout):
                    build.main()

            html = (base / "index.html").read_text(encoding="utf-8")

            self.assertIn("Playwright MCP", html)
            self.assertIn("Codex for Claude Code", html)
            self.assertIn("6 ferramentas", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
