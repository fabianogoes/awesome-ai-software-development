#!/usr/bin/env python3
"""Executa verificações leves após edições feitas pelo Claude Code."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REBUILD_FILES = {
    "README.md",
    "CONCEPTS.md",
    "BOOKS.md",
    "CLAUDE_TIPS.md",
    "docs/purpose.md",
    "docs/shared-resources.md",
}
TEST_FILES = {
    "src/build.py",
    "src/test_build.py",
    "src/test_claude_post_edit_check.py",
    "tools/scripts/claude_post_edit_check.py",
}


def determine_actions(changed_files):
    """Retorna a lista de comandos a executar com base nos arquivos alterados."""
    normalized = {Path(path).as_posix() for path in changed_files if path}
    actions = []

    if normalized & REBUILD_FILES:
        actions.append(("python3", "src/build.py"))
    if normalized & TEST_FILES:
        actions.append(
            ("python3", "-m", "unittest", "discover", "-s", "src", "-p", "test*.py", "-v")
        )

    return actions


def get_changed_files():
    """Lê o diff atual do repositório para decidir quais validações disparar."""
    result = subprocess.run(
        ["git", "diff", "--name-only"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def run_action(action):
    """Executa um comando de validação e retorna o código de saída."""
    print(f"[claude-post-edit] executando: {' '.join(action)}")
    result = subprocess.run(action, check=False)
    return result.returncode


def main():
    try:
        changed_files = get_changed_files()
    except subprocess.CalledProcessError as exc:
        print(f"[claude-post-edit] não foi possível ler o diff: {exc}", file=sys.stderr)
        return 1

    actions = determine_actions(changed_files)
    if not actions:
        print("[claude-post-edit] nenhuma verificação adicional necessária.")
        return 0

    exit_code = 0
    for action in actions:
        result = run_action(action)
        if result != 0:
            exit_code = result

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
