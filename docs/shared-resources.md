# Recursos Compartilhados

Catalogo publico de recursos que podem ser reaproveitados em outros projetos e por diferentes agentes.

## Skills

- `claude-project-setup`: skill para bootstrap de uma estrutura agnostica de agentes

## Agents

- `reviewer`: template inicial para revisao com foco em bugs, riscos, regressao e lacunas de teste

## Plugins

- o repositorio documenta plugins e integracoes uteis no catalogo principal
- recursos compartilhados devem evitar dependencia exclusiva de uma ferramenta

## Convencoes

- `.agents/` e a fonte de verdade para recursos compartilhados entre agentes
- `AGENTS.md` e o contexto global compartilhado
- `.claude/` e `CLAUDE.md` existem como compatibilidade
- `.agents/commands/` e a origem canonica dos commands
- `.claude/commands/` permanece como wrapper minimo de compatibilidade

## Instalar a skill de setup

### Via scripts do projeto

- Linux/macOS: `bash scripts/setup-agents.sh full`
- Windows CMD: `scripts\setup-agents.cmd full`
- Windows PowerShell: `powershell -ExecutionPolicy Bypass -File .\scripts\setup-agents.ps1 -Profile full`

### O que o setup cria

- estrutura base em `.agents/`
- `AGENTS.md` com contexto inicial
- aliases de compatibilidade para Claude
- templates publicos e operacionais do perfil `full`
