# Public Private Structure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reorganizar o repositório para refletir a estrutura agnóstica de agentes, centralizar comandos em `.agents/commands/` e expandir o build público para incluir conteúdo compartilhável como `CLAUDE_TIPS.md`, `docs/purpose.md` e `docs/shared-resources.md`.

**Architecture:** `.agents/` vira a fonte canônica para comandos e regras, com compatibilidade preservada para Claude. O build público continua controlado por `src/build.py`, mas passa a renderizar apenas documentos públicos e genéricos. Documentação operacional interna permanece fora do site.

**Tech Stack:** Python `unittest`, Python standard library, Markdown, HTML gerado por `src/build.py`.

---

### Task 1: Proteger a nova convenção com testes

**Files:**
- Modify: `src/test_setup_scripts.py`
- Modify: `src/test_build.py`
- Create: `src/test_project_structure.py`

**Step 1: Write the failing tests**

Adicionar testes que falhem se:
- a convenção de comandos canônicos em `.agents/commands/` não estiver documentada em uma rule
- `CLAUDE.md` deixar de apontar para `AGENTS.md`
- o build não incluir `CLAUDE_TIPS.md`
- o build não suportar `docs/purpose.md` e `docs/shared-resources.md`
- conteúdo interno indevido começar a aparecer no site público

**Step 2: Run tests to verify they fail**

Run: `python3 -m unittest discover -s src -p 'test*.py' -v`
Expected: FAIL

### Task 2: Alinhar a estrutura de agentes

**Files:**
- Create: `.agents/commands/`
- Create: `.agents/rules/commands-source-of-truth.md`
- Modify: `.claude/commands/rebuild.md`
- Modify: `.claude/commands/release-check.md`
- Modify: `.claude/commands/test.md`

**Step 1: Implement canonical commands**

- mover ou recriar os comandos atuais em `.agents/commands/`
- transformar `.claude/commands/` em compatibilidade leve
- adicionar a rule formalizando a convenção

**Step 2: Verify structure**

Run: `python3 -m unittest discover -s src -p 'test*.py' -v`
Expected: tests estruturais passam

### Task 3: Centralizar scripts por papel

**Files:**
- Modify: `scripts/setup-agents.sh`
- Modify: `scripts/setup-agents.ps1`
- Modify: `scripts/setup-agents.cmd`
- Possibly modify: `tools/scripts/claude_post_edit_check.py`
- Possibly create: `docs/shared-resources.md`

**Step 1: Clarify script responsibilities**

- manter `scripts/` para bootstrap, setup e templates
- manter `tools/scripts/` para automações operacionais do projeto
- documentar essa convenção em `docs/shared-resources.md`

**Step 2: Verify references**

Run: `python3 -m unittest discover -s src -p 'test*.py' -v`
Expected: PASS

### Task 4: Criar documentação pública nova

**Files:**
- Create: `docs/purpose.md`
- Create: `docs/shared-resources.md`
- Modify: `README.md`
- Modify: `CLAUDE_TIPS.md`

**Step 1: Write public docs**

- `docs/purpose.md`: propósito, escopo e princípios do projeto
- `docs/shared-resources.md`: skills, agents, plugins e help para instalar a skill de setup
- manter `README.md` genérico e não operacional

**Step 2: Review public/private split**

Confirmar que os documentos novos são públicos e genéricos, sem expor detalhes internos indevidos.

### Task 5: Expandir o build público

**Files:**
- Modify: `src/build.py`
- Modify: `src/test_build.py`
- Modify: `README.md`
- Modify: `index.html`

**Step 1: Add new public sections**

- incluir `CLAUDE_TIPS.md`
- incluir `docs/purpose.md`
- incluir `docs/shared-resources.md`
- organizar a UI para separar catálogo, propósito, recursos e tips

**Step 2: Verify build**

Run: `python3 src/build.py`
Expected: `index.html` gerado sem erro e com as novas seções públicas

### Task 6: Verificação final

**Files:**
- Modify: `index.html`

**Step 1: Run full verification**

Run: `python3 -m unittest discover -s src -p 'test*.py' -v`
Expected: PASS

**Step 2: Rebuild final output**

Run: `python3 src/build.py`
Expected: `index.html` sincronizado com o conteúdo final
