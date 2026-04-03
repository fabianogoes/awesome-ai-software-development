# CLAUDE_TIPS.md

Dicas e referências rápidas para usar melhor o Claude Code.

## Tips

- [10 Claude Code tips from Boris, the creator of Claude Code, summarized](https://ykdojo.github.io/claude-code-tips/content/boris-claude-code-tips)
- [Modo interativo - Referência completa para atalhos de teclado, modos de entrada e recursos interativos em sessões do Claude Code.](https://code.claude.com/docs/pt/interactive-mode)
- [Estrutura de Projeto Claude Code - 10 insights para estruturar projetos com Claude Code](https://www.linkedin.com/posts/luciola-coelho-agencia-de-ia_claudemd-share-7441180082175467520-99ks/)

## Estrutura proposta para projetos que usam CLAUDE

Uma estrutura modular útil para projetos com Claude Code combina memória do projeto, workflows reutilizáveis, documentação operacional e automações leves.

```text
projeto/
├── CLAUDE.md
├── README.md
├── docs/
│   ├── architecture.md
│   ├── decisions/
│   └── runbooks/
├── .claude/
│   ├── settings.json
│   ├── commands/
│   └── hooks/
├── src/
├── tools/
│   ├── scripts/
│   └── prompts/
└── images/
```

### Componentes-chave

- `CLAUDE.md`: memória compartilhada do projeto, com contexto, comandos principais e regras de trabalho.
- `.claude/settings.json`: configurações versionadas do Claude Code para o projeto.
- `.claude/commands/`: comandos reutilizáveis para tarefas recorrentes.
- `.claude/hooks/`: guardrails, validações e automações disparadas pelo fluxo do Claude Code.
- `docs/architecture.md`: visão arquitetural do projeto.
- `docs/decisions/`: registro de decisões arquiteturais.
- `docs/runbooks/`: procedimentos operacionais para tarefas recorrentes.
- `src/`: código-fonte, scripts principais e testes do projeto.
- `tools/scripts/`: automações auxiliares e utilitários.
- `tools/prompts/`: prompts reutilizáveis quando fizer sentido para o workflow.

### Boas práticas

- Mantenha o `CLAUDE.md` curto, focado e atualizado.
- Separe contexto do projeto de automações e de documentação arquitetural.
- Use `commands` e `hooks` para tarefas repetitivas e verificações simples.
- Documente decisões importantes em `docs/decisions/`.
- Evite estruturar o repositório de forma artificial; adapte a árvore ao tipo real de projeto.
- Preserve arquivos gerados como artefatos, não como fonte de verdade.

### Dicas de desenvolvimento

- Mantenha prompts modulares e fáceis de reutilizar.
- Mantenha a estrutura do repositório limpa e previsível.
- Use skills e comandos para workflows recorrentes.
- Use hooks para automatizar verificações e guardrails.
- Documente arquitetura, decisões e runbooks operacionais.
