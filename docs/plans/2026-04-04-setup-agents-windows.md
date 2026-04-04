# Setup Agents Windows Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Corrigir a experiência de setup no Windows e remover a criação de `.clinerules` dos scripts de bootstrap.

**Architecture:** Manter `scripts/setup-agents.ps1` como implementação principal no Windows, adicionar um wrapper `scripts/setup-agents.cmd` para executar o PowerShell com `ExecutionPolicy Bypass` apenas no processo atual, e alinhar a documentação. Proteger o comportamento com testes simples que validam o conteúdo dos scripts.

**Tech Stack:** Python `unittest`, shell script Bash, PowerShell, CMD.

---

### Task 1: Cobrir os scripts com testes

**Files:**
- Create: `src/test_setup_scripts.py`

**Step 1: Write the failing test**

Criar testes que:
- falhem se `scripts/setup-agents.sh` mencionar `.clinerules`
- falhem se `scripts/setup-agents.ps1` mencionar `.clinerules`
- falhem se `scripts/setup-agents.cmd` não existir ou não usar `ExecutionPolicy Bypass`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest src.test_setup_scripts -v`
Expected: FAIL porque o wrapper `.cmd` ainda não existe e os scripts atuais ainda criam `.clinerules`.

### Task 2: Ajustar os scripts

**Files:**
- Modify: `scripts/setup-agents.sh`
- Modify: `scripts/setup-agents.ps1`
- Create: `scripts/setup-agents.cmd`

**Step 1: Write minimal implementation**

- remover `.clinerules` da criação inicial nos scripts Bash e PowerShell
- adicionar comentários/instruções curtas no `.ps1`
- criar `setup-agents.cmd` chamando `powershell -ExecutionPolicy Bypass -File`

**Step 2: Run test to verify it passes**

Run: `python3 -m unittest src.test_setup_scripts -v`
Expected: PASS

### Task 3: Atualizar documentação e verificar tudo

**Files:**
- Modify: `README.md`
- Modify: `index.html`

**Step 1: Update docs**

Adicionar instruções curtas de uso para Linux/macOS, PowerShell e CMD no Windows.

**Step 2: Rebuild generated output**

Run: `python3 src/build.py`
Expected: `index.html` regenerado sem erros.

**Step 3: Run full verification**

Run: `python3 -m unittest discover -s src -p 'test*.py' -v`
Expected: PASS
