# Repository Guidelines

## Agent Communication

All communication with maintainers and contributors must be in Brazilian Portuguese (`pt-BR`). Keep messages, reviews, status updates, and pull request descriptions in `pt-BR`, unless a specific task explicitly requires another language.

## Project Structure & Module Organization

This repository is markdown-first. `README.md`, `CONCEPTS.md`, `BOOKS.md`, `CLAUDE_TIPS.md`, [`docs/purpose.md`](/home/fabiano/projects/awesome-ai-software-development/docs/purpose.md), and [`docs/shared-resources.md`](/home/fabiano/projects/awesome-ai-software-development/docs/shared-resources.md) are the public content sources; [`src/build.py`](/home/fabiano/projects/awesome-ai-software-development/src/build.py) generates `index.html` for GitHub Pages. Keep images in `images/`, and treat `index.html` as generated output, not an editing target. Tests live in [`src/test_build.py`](/home/fabiano/projects/awesome-ai-software-development/src/test_build.py).

## Build, Test, and Development Commands

- `python3 src/build.py`: regenerate `index.html` from the markdown sources.
- `python3 -m unittest discover -s src -p 'test*.py' -v`: run the parser and HTML-generation tests.
- `python3 -m http.server 3000`: preview the generated site locally at `http://localhost:3000`.

Run `python3 src/build.py` after any content or parser change so generated output stays in sync.

## Coding Style & Naming Conventions

Use 4-space indentation in Python and follow existing standard-library-only style. Prefer small pure functions, `snake_case` for functions and variables, and short docstrings where behavior is not obvious. In markdown content, preserve the current table schemas exactly, for example `| Ferramenta | Descrição | Link | Avaliação |`, because the parser depends on those headers.

## Testing Guidelines

Add or update `unittest` cases whenever changing parsing logic, section names, or generated HTML behavior. Name tests with the `test_*` pattern and keep fixtures minimal and inline, as in [`src/test_build.py`](/home/fabiano/projects/awesome-ai-software-development/src/test_build.py). For content-only edits, rebuild locally and sanity-check the rendered `index.html`.

## Commit & Pull Request Guidelines

Recent history favors short, imperative commit subjects such as `update github page`, `Add Agency Agents section to README`, and `Atualizar o README.md`. Keep commits focused and descriptive; use either English or Portuguese, but stay consistent within a commit. PRs should summarize the changed sections, note whether `index.html` was regenerated, link related issues when applicable, and include a screenshot only when the rendered page changes visually.

## Publishing Workflow

GitHub Actions publishes Pages from `main` via `.github/workflows/pages.yml`. Changes to public content sources such as `README.md`, `CONCEPTS.md`, `BOOKS.md`, `CLAUDE_TIPS.md`, [`docs/purpose.md`](/home/fabiano/projects/awesome-ai-software-development/docs/purpose.md), [`docs/shared-resources.md`](/home/fabiano/projects/awesome-ai-software-development/docs/shared-resources.md), or [`src/build.py`](/home/fabiano/projects/awesome-ai-software-development/src/build.py) should include the regenerated `index.html` in the same branch.
