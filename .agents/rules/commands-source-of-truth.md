# Commands Source Of Truth

## Rule

- `.agents/commands/` e a fonte de verdade para commands versionados do projeto.
- `.claude/commands/` existe apenas para compatibilidade com Claude Code.
- Novos commands devem nascer primeiro em `.agents/commands/`.
- Qualquer espelho em `.claude/commands/` deve apontar para o comando canonico ou resumir que a origem esta em `.agents/commands/`.

## Motivation

- reduz acoplamento com uma ferramenta especifica
- preserva a estrutura agnostica do projeto
- facilita reuso por outros agentes
