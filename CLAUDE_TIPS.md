# CLAUDE_TIPS.md

Dicas e referências rápidas para usar melhor o Claude Code.

## Referências

Links para leitura rápida, inspiração e consulta oficial sobre Claude Code.

- [10 Claude Code tips from Boris, the creator of Claude Code, summarized](https://ykdojo.github.io/claude-code-tips/content/boris-claude-code-tips)
- [Modo interativo - Referência completa para atalhos de teclado, modos de entrada e recursos interativos em sessões do Claude Code.](https://code.claude.com/docs/pt/interactive-mode)
- [Estrutura de Projeto Claude Code - 10 insights para estruturar projetos com Claude Code](https://www.linkedin.com/posts/luciola-coelho-agencia-de-ia_claudemd-share-7441180082175467520-99ks/)
- [CLI usage - documentação oficial da Anthropic para uso da CLI do Claude Code.](https://docs.anthropic.com/en/docs/claude-code/cli-usage)
- [Dev Containers - guia oficial para uso do Claude Code em ambientes isolados.](https://docs.anthropic.com/pt/docs/claude-code/devcontainer)

## Comandos Úteis

Comandos e flags que valem conhecer antes de automatizar ou operar o Claude Code no dia a dia.

- `claude --dangerously-skip-permissions`: pula prompts de permissão. É útil para automação e execução desassistida, mas só deve ser usado em repositórios confiáveis e ambientes bem controlados.

## Fluxos Práticos

Dicas para transformar o Claude Code em parte do workflow do projeto, e não apenas em uma ferramenta ocasional.

- Separe claramente o que é contexto compartilhado do projeto (`AGENTS.md`) do que é compatibilidade com uma ferramenta específica (`CLAUDE.md`, `.claude/`).
- Use `.agents/commands/` como origem dos comandos do projeto e trate `.claude/commands/` apenas como compatibilidade.
- Mantenha documentação pública, regras internas e automações operacionais em lugares diferentes para evitar acoplamento desnecessário.
- Quando o projeto tiver GitHub Pages, publique apenas conteúdo curado e público; não exponha estruturas internas por acidente.
- Prefira evoluir templates e scripts de bootstrap de forma centralizada, para manter o setup reproduzível entre ferramentas e sistemas operacionais.
- Trate comandos, skills e regras como produtos compartilháveis: se algo puder ser reutilizado por outras pessoas, documente e promova isso explicitamente.

## Estrutura proposta para projetos que usam CLAUDE

Uma estrutura modular útil para projetos com Claude Code e outras ferramentas de agentes combina uma fonte de verdade agnóstica, aliases de compatibilidade, documentação pública e automações operacionais bem separadas.

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
│   ├── purpose.md
│   ├── shared-resources.md
│   ├── architecture.md
│   ├── decisions/
│   └── runbooks/
├── src/
├── scripts/
│   ├── setup-agents.sh
│   ├── setup-agents.ps1
│   ├── setup-agents.cmd
│   └── templates/
├── tools/
│   ├── scripts/
│   └── prompts/
└── images/
```

### Componentes-chave

- `.agents/`: fonte da verdade para comandos, skills, regras e outros artefatos compartilhados entre agentes.
- `.agents/commands/`: origem canônica dos comandos do projeto.
- `AGENTS.md`: memória compartilhada principal do projeto, com contexto, comandos e diretrizes globais.
- `CLAUDE.md`: alias de compatibilidade apontando para `AGENTS.md`.
- `.claude`: alias de compatibilidade apontando para `.agents/`.
- `docs/purpose.md`: propósito, escopo e princípios públicos do repositório.
- `docs/shared-resources.md`: catálogo público de skills, agents, plugins e convenções compartilháveis.
- `docs/architecture.md`: visão arquitetural do projeto.
- `docs/decisions/`: registro de decisões arquiteturais.
- `docs/runbooks/`: procedimentos operacionais para tarefas recorrentes.
- `scripts/`: bootstrap e templates versionados da estrutura agnóstica.
- `src/`: código-fonte, scripts principais e testes do projeto.
- `tools/scripts/`: automações operacionais e utilitários internos do projeto.
- `tools/prompts/`: prompts reutilizáveis quando fizer sentido para o workflow.
- `scripts/templates/`: templates versionados usados pelo bootstrap para gerar `AGENTS.md`, ADRs, onboarding e regras iniciais.

### Boas práticas

- Mantenha o `AGENTS.md` curto, focado e atualizado.
- Separe contexto do projeto, documentação pública e automações operacionais.
- Trate `.agents/` como a estrutura compartilhada e use aliases apenas para compatibilidade.
- Faça novos comandos nascerem em `.agents/commands/`; `.claude/commands/` deve existir apenas como compatibilidade.
- Use `commands`, `skills` e `rules` para tarefas repetitivas, guardrails e verificações simples.
- Documente decisões importantes em `docs/decisions/`.
- Mantenha `README.md` genérico e público; instruções internas devem ficar fora da página principal.
- Evolua o bootstrap editando `scripts/templates/`, em vez de espalhar conteúdo inline em vários scripts.
- Evite estruturar o repositório de forma artificial; adapte a árvore ao tipo real de projeto.
- Preserve arquivos gerados como artefatos, não como fonte de verdade.
- Se um recurso for pensado para compartilhamento, descreva-o em `docs/shared-resources.md` antes de tratá-lo como parte do setup padrão.

### Dicas de Desenvolvimento

- Mantenha prompts modulares e fáceis de reutilizar.
- Mantenha a estrutura do repositório limpa e previsível.
- Use skills e comandos para workflows recorrentes.
- Use hooks para automatizar verificações e guardrails.
- Documente arquitetura, decisões e runbooks operacionais.

## Uso com cuidado: `claude --dangerously-skip-permissions`

Segundo a documentação oficial do Claude Code, a flag `--dangerously-skip-permissions` inicia o Claude sem prompts de permissão. Isso pode ser útil em automações, scripts e execuções desassistidas, principalmente em ambientes isolados como devcontainers.

Exemplo de uso:

```bash
claude --dangerously-skip-permissions
```

Alertas importantes:

- Use essa opção apenas quando você entender exatamente quais comandos e acessos o Claude poderá executar sem confirmação.
- A documentação oficial recomenda cautela explícita no uso dessa flag.
- No guia de devcontainers, a Anthropic explica que nem mesmo um ambiente isolado impede totalmente que um projeto malicioso exfiltre dados acessíveis no ambiente, incluindo credenciais do Claude Code.
- Prefira esse modo apenas em repositórios confiáveis e, de preferência, dentro de ambientes isolados e controlados.

Referências oficiais:

- CLI reference: <https://docs.anthropic.com/en/docs/claude-code/cli-usage>
- Dev Containers: <https://docs.anthropic.com/pt/docs/claude-code/devcontainer>
