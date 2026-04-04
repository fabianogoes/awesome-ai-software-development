---
name: claude-project-setup
description: Use when the user asks to initialize an AI coding project, prepare a repository for Claude Code, or create a shared agent structure with compatibility across tools like Claude, Codex, and similar agents.
---

# Claude Project Setup

Esta skill orienta a criacao de uma estrutura agnostica para projetos com agentes de IA.

## Visao geral

A fonte da verdade deve ser:
- `.agents/` para comandos, skills, regras e extensoes do ecossistema
- `AGENTS.md` para contexto global compartilhado

A compatibilidade deve ser exposta por alias:
- `.claude` apontando para `.agents/`
- `.codex` apontando para `.agents/`
- `CLAUDE.md` apontando para `AGENTS.md`

Evite manter arvores paralelas como fonte principal. A ideia e centralizar o que e comum e usar links ou aliases para compatibilidade por ferramenta.

## Perfis de setup

### `minimal`

Use para bootstrap enxuto ou repositorios que ainda estao nascendo.

Estrutura esperada:

```text
projeto/
├── .agents/
│   ├── agents/
│   ├── commands/
│   ├── skills/
│   └── rules/
├── .claude -> .agents
├── .codex -> .agents
├── AGENTS.md
├── CLAUDE.md -> AGENTS.md
├── docs/
│   └── architecture.md
└── src/
```

### `standard`

Use para repositorios que ja querem uma base operacional mais completa.

Adiciona ao perfil `minimal`:
- `docs/decisions/`
- `docs/runbooks/`
- `docs/PRD.md`
- `docs/Plan.md`
- `docs/Napkin.md`
- `tools/scripts/`
- `tools/prompts/`
- `images/`
- `.agents/hooks/`
- `.agents/settings/`

### `full`

Use quando o repositorio ja precisa nascer com convencoes para colaboracao entre pessoas e agentes.

Adiciona ao perfil `standard`:
- `docs/decisions/0001-template.md`
- `docs/runbooks/onboarding.md`
- `.agents/agents/reviewer.md`
- `.agents/rules/code-review.md`

## Como executar

### 1. Determinar o diretorio raiz

Se o usuario nao especificou, assuma o diretorio atual.

### 2. Verificar o que ja existe

Antes de criar qualquer coisa:
- liste arquivos e diretorios relevantes
- identifique o que ja existe
- crie apenas o que estiver ausente
- nunca sobrescreva arquivos de contexto que o projeto ja tenha preenchido

### 3. Criar a estrutura

Se o usuario pediu automacao direta, prefira chamar os scripts do repositorio:
- Linux/macOS: `bash scripts/setup-agents.sh`
- Linux/macOS perfil completo: `bash scripts/setup-agents.sh standard`
- Linux/macOS perfil full: `bash scripts/setup-agents.sh full`
- Windows CMD: `scripts\setup-agents.cmd`
- Windows CMD perfil completo: `scripts\setup-agents.cmd standard`
- Windows CMD perfil full: `scripts\setup-agents.cmd full`
- Windows PowerShell: `powershell -ExecutionPolicy Bypass -File .\scripts\setup-agents.ps1`
- Windows PowerShell perfil completo: `powershell -ExecutionPolicy Bypass -File .\scripts\setup-agents.ps1 -Profile standard`
- Windows PowerShell perfil full: `powershell -ExecutionPolicy Bypass -File .\scripts\setup-agents.ps1 -Profile full`

Se nao houver script disponivel, replique manualmente a mesma estrutura.

Os conteudos padrao do bootstrap ficam versionados em `scripts/templates/`:
- `scripts/templates/common/AGENTS.md` para o contexto inicial compartilhado
- `scripts/templates/full/` para ADR, onboarding e templates de revisao do perfil `full`

Isso permite evoluir o bootstrap ajustando os templates sem precisar manter blocos grandes inline nos scripts.

### 4. Semantica dos arquivos principais

- `AGENTS.md`: contexto global compartilhado e canonico
- `CLAUDE.md`: alias de compatibilidade, nao a fonte principal
- `.agents/commands/`: automacoes e atalhos reutilizaveis
- `.agents/skills/`: habilidades e instrucoes especializadas
- `.agents/rules/`: guardrails e politicas do projeto
- `docs/architecture.md`: visao arquitetural de alto nivel
- `docs/decisions/`: historico de decisoes importantes
- `docs/runbooks/`: operacao, incidentes e procedimentos recorrentes

## Relatorio final

Ao concluir, informe:
- o que ja existia
- o que foi criado agora
- qual perfil foi aplicado: `minimal`, `standard` ou `full`
- quais aliases de compatibilidade foram criados
- quais proximos passos o usuario deve preencher manualmente

## Boas praticas

- mantenha `AGENTS.md` curto e importando documentos mais pesados
- trate `.agents/` como estrutura compartilhada entre ferramentas
- use `standard` quando o projeto precisar de governanca e operacao desde o inicio
- use `full` quando quiser templates iniciais para onboarding, ADR e revisao
- use `minimal` quando a prioridade for velocidade e baixo atrito
- mantenha `scripts/templates/` como fonte versionada dos conteudos iniciais do bootstrap
- adapte a estrutura ao contexto real do repositorio em vez de criar pastas sem uso
