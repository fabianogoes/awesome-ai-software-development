# ADR 0001: Estrutura operacional para Claude Code

## Status

Aceita

## Contexto

O repositório já tinha um fluxo simples e funcional, mas não possuía uma camada explícita de contexto compartilhado, comandos reutilizáveis e automações leves para agentes. Ao mesmo tempo, mover o núcleo do projeto para uma estrutura típica de aplicação introduziria complexidade artificial.

## Decisão

Manter `README.md`, `CONCEPTS.md`, `BOOKS.md`, `src/build.py` e `index.html` nos papéis atuais e adicionar uma camada operacional inspirada em projetos Claude Code:

- `CLAUDE.md` na raiz para memória compartilhada.
- `.claude/` para settings, hooks e comandos.
- `docs/` para arquitetura, ADRs e runbooks.
- `tools/scripts/` para automações leves reutilizáveis.

## Consequências

- O workflow público e o build continuam simples.
- Agentes passam a ter contexto e guardrails explícitos no próprio repositório.
- O projeto ganha organização operacional sem forçar uma migração para `src/`.
