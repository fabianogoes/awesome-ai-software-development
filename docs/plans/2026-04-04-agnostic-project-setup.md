# Agnostic Project Setup Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Consolidar a skill de setup de projeto e os scripts de bootstrap em uma arquitetura agnóstica, com perfis `minimal` e `standard`.

**Architecture:** Os scripts continuam sendo o mecanismo de bootstrap físico do projeto, criando `.agents/`, `AGENTS.md` e links de compatibilidade. A skill passa a orientar a arquitetura agnóstica e os dois perfis de setup, herdando da versão anterior apenas os diretórios úteis como `docs/decisions`, `docs/runbooks`, `tools/scripts`, `tools/prompts` e `images`.

**Tech Stack:** Bash, PowerShell, CMD, Python `unittest`, Markdown.

---

### Task 1: Cobrir a nova intenção com testes

**Files:**
- Modify: `src/test_setup_scripts.py`

**Step 1: Write the failing test**

Adicionar testes que falhem se:
- os scripts não aceitarem um perfil `standard`
- os scripts não incluírem criação de `docs/decisions`, `docs/runbooks`, `tools/scripts`, `tools/prompts` e `images`
- a skill não mencionar `AGENTS.md` como fonte da verdade e `.agents/` como estrutura principal

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest src.test_setup_scripts -v`
Expected: FAIL

### Task 2: Implementar perfis nos scripts

**Files:**
- Modify: `scripts/setup-agents.sh`
- Modify: `scripts/setup-agents.ps1`
- Modify: `scripts/setup-agents.cmd`

**Step 1: Write minimal implementation**

- perfil default `minimal`
- suporte a `standard`
- `minimal`: `.agents/`, `AGENTS.md`, `docs/architecture.md`, `src/`, links
- `standard`: adiciona `docs/decisions`, `docs/runbooks`, `tools/scripts`, `tools/prompts`, `images`, `PRD.md`, `Plan.md`, `Napkin.md`

**Step 2: Run test to verify it passes**

Run: `python3 -m unittest src.test_setup_scripts -v`
Expected: PASS

### Task 3: Reescrever a skill

**Files:**
- Modify: `skills/claude-project-setup/SKILL.md`

**Step 1: Update skill content**

Reescrever a skill para:
- orientar uma arquitetura agnóstica
- tratar `.agents/` e `AGENTS.md` como canônicos
- explicar links de compatibilidade para `.claude`, `.codex` e `CLAUDE.md`
- apresentar os perfis `minimal` e `standard`

**Step 2: Run verification**

Run: `python3 -m unittest src.test_setup_scripts -v`
Expected: PASS

### Task 4: Verificação final

**Files:**
- Modify: `README.md` (se necessário)
- Modify: `index.html` (se `README.md` mudar)

**Step 1: Run full verification**

Run: `python3 -m unittest discover -s src -p 'test*.py' -v`
Expected: PASS

**Step 2: Rebuild generated output if docs changed**

Run: `python3 src/build.py`
Expected: `index.html` atualizado sem erros, apenas se `README.md` for alterado.
