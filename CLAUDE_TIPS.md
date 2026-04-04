# CLAUDE_TIPS.md

Dicas e referências rápidas para usar melhor o Claude Code.

## Tips

- [10 Claude Code tips from Boris, the creator of Claude Code, summarized](https://ykdojo.github.io/claude-code-tips/content/boris-claude-code-tips)
- [Modo interativo - Referência completa para atalhos de teclado, modos de entrada e recursos interativos em sessões do Claude Code.](https://code.claude.com/docs/pt/interactive-mode)
- [Estrutura de Projeto Claude Code - 10 insights para estruturar projetos com Claude Code](https://www.linkedin.com/posts/luciola-coelho-agencia-de-ia_claudemd-share-7441180082175467520-99ks/)
- [`claude --dangerously-skip-permissions` - opção da CLI para pular prompts de permissão; útil para automação e operação desassistida, mas deve ser usada com muito cuidado. Referências oficiais: CLI reference e Dev Containers.](https://docs.anthropic.com/en/docs/claude-code/cli-usage)

## Estrutura proposta para projetos que usam CLAUDE

Uma estrutura modular útil para projetos com Claude Code e outras ferramentas de agentes combina uma fonte de verdade agnóstica, aliases de compatibilidade, documentação operacional e automações leves.

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
│   ├── architecture.md
│   ├── decisions/
│   └── runbooks/
├── src/
├── tools/
│   ├── scripts/
│   └── prompts/
├── images/
└── scripts/
    └── templates/
```

### Componentes-chave

- `.agents/`: fonte da verdade para comandos, skills, regras e outros artefatos compartilhados entre agentes.
- `AGENTS.md`: memória compartilhada principal do projeto, com contexto, comandos e diretrizes globais.
- `CLAUDE.md`: alias de compatibilidade apontando para `AGENTS.md`.
- `.claude`: alias de compatibilidade apontando para `.agents/`.
- `docs/architecture.md`: visão arquitetural do projeto.
- `docs/decisions/`: registro de decisões arquiteturais.
- `docs/runbooks/`: procedimentos operacionais para tarefas recorrentes.
- `src/`: código-fonte, scripts principais e testes do projeto.
- `tools/scripts/`: automações auxiliares e utilitários.
- `tools/prompts/`: prompts reutilizáveis quando fizer sentido para o workflow.
- `scripts/templates/`: templates versionados usados pelo bootstrap para gerar `AGENTS.md`, ADRs, onboarding e regras iniciais.

### Boas práticas

- Mantenha o `AGENTS.md` curto, focado e atualizado.
- Separe contexto do projeto de automações e de documentação arquitetural.
- Trate `.agents/` como a estrutura compartilhada e use aliases apenas para compatibilidade.
- Use `commands`, `skills` e `rules` para tarefas repetitivas e verificações simples.
- Documente decisões importantes em `docs/decisions/`.
- Evolua o bootstrap editando `scripts/templates/`, em vez de espalhar conteúdo inline em vários scripts.
- Evite estruturar o repositório de forma artificial; adapte a árvore ao tipo real de projeto.
- Preserve arquivos gerados como artefatos, não como fonte de verdade.

### Dicas de desenvolvimento

- Mantenha prompts modulares e fáceis de reutilizar.
- Mantenha a estrutura do repositório limpa e previsível.
- Use skills e comandos para workflows recorrentes.
- Use hooks para automatizar verificações e guardrails.
- Documente arquitetura, decisões e runbooks operacionais.

## Uso com cuidado: `claude --dangerously-skip-permissions`

Segundo a documentação oficial do Claude Code, a flag `--dangerously-skip-permissions` inicia o Claude sem prompts de permissão. Isso pode ser útil em automações, scripts e execuções desassistidas, principalmente em ambientes isolados como devcontainers.

Exemplo:

```bash
claude --dangerously-skip-permissions
```

Alerta importante:

- Use essa opção apenas quando você entender exatamente quais comandos e acessos o Claude poderá executar sem confirmação.
- A documentação oficial recomenda cautela explícita no uso dessa flag.
- No guia de devcontainers, a Anthropic explica que nem mesmo um ambiente isolado impede totalmente que um projeto malicioso exfiltre dados acessíveis no ambiente, incluindo credenciais do Claude Code.
- Prefira esse modo apenas em repositórios confiáveis e, de preferência, dentro de ambientes isolados e controlados.

Referências oficiais:

- CLI reference: <https://docs.anthropic.com/en/docs/claude-code/cli-usage>
- Dev Containers: <https://docs.anthropic.com/pt/docs/claude-code/devcontainer>
