# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a curated "awesome list" — a Markdown-only repository with no build system, dependencies, or tests. All content lives in `README.md`.

## Contributing

Changes consist solely of editing `README.md` to add, update, or remove entries. The list is organized into sections:

- **Tools** — Code assistants, IDEs, Frameworks/Libs
- **Books** — (currently empty, marked `???`)
- **Blog Posts** — Written articles and videos
- **Utils** — Useful references and methodologies
- **Concepts** — Definitions of AI/LLM-related terms (mostly empty, marked `???`)
- **Mentors** — (referenced in TOC but not yet present)

Entries marked `???` are placeholders awaiting content contributions.

## Format Conventions

- Section headers use `##` and `###`
- Each entry is a Markdown link: `- [Name](URL)`
- The Table of Contents uses checkboxes (`- [x]`) linked to section anchors
- License badge is an image link at the bottom (`MIT.png`)

## Skills

- [Claude Code Skills](https://code.claude.com/docs/pt/skills)
- [Agent Skills](https://agentskills.io/home)

## MCP
Aprenda como conectar o Claude Code às suas ferramentas com o Model Context Protocol.

Claude Code pode se conectar a centenas de ferramentas externas e fontes de dados por meio do Model Context Protocol (MCP), um padrão de código aberto para integrações de ferramentas de IA. Os servidores MCP dão ao Claude Code acesso às suas ferramentas, bancos de dados e APIs.

[Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)

| MCP                | Descrição                                                                                                                     | Link                                        | ...         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ----------- |
| Grafana MCP server | This provides access to your Grafana instance and the surrounding ecosystem.                                                  | https://github.com/grafana/mcp-grafana      | :hourglass: |
| Playwright MCP     | Servidor MCP de automação de navegador e testes E2E com Playwright, permitindo que LLMs interajam com páginas via snapshots de acessibilidade. | https://github.com/microsoft/playwright-mcp | :hourglass: |
| Firecrawl          | Plugin para o Claude Code que permite rastrear e extrair conteúdo da web (crawling/scraping) para alimentar fluxos de trabalho e agentes com dados atualizados. | https://www.firecrawl.dev/integrations/claude-code | :hourglass: |
| Netlify MCP Server | Dê aos agentes de código a capacidade de construir, implantar e muito mais com o Netlify MCP Server.                          | https://docs.netlify.com/build/build-with-ai/netlify-mcp-server/ | :hourglass: |

### MCP Installation

```bash
claude mcp add --transport sse atlasian https://mcp.atlassian.com/v1/sse -s user
claude mcp add --transport http gh https://api.githubcopilot.com/mcp -H "Authorization: Bearer <GITHUB_TOKEN>"
claude mcp add --transport http datadog-mcp https://mcp.us5.datadoghq.com/api/unstable/mcp-server/mcp
claude mcp add playwright npx @playwright/mcp@latest
claude mcp add --transport http netlify https://netlify-mcp.netlify.app/mcp
```

## Plugins

| MCP                | Descrição                                                                                                                     | Link                                        | ...         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ----------- |
| Firecrawl          | Plugin para o Claude Code que permite rastrear e extrair conteúdo da web (crawling/scraping) para alimentar fluxos de trabalho e agentes com dados atualizados. | https://www.firecrawl.dev/integrations/claude-code | :hourglass: |

```bash
claude plugin install firecrawl@claude-plugins-official
```

## Tips

- [10 Claude Code tips from Boris, the creator of Claude Code, summarized](https://ykdojo.github.io/claude-code-tips/content/boris-claude-code-tips)
- [Modo interativo - Referência completa para atalhos de teclado, modos de entrada e recursos interativos em sessões do Claude Code.](https://code.claude.com/docs/pt/interactive-mode)
- [Estrutura de Projeto Claude Code - 10 insights para estruturar projetos com Claude Code](https://www.linkedin.com/posts/luciola-coelho-agencia-de-ia_claudemd-share-7441180082175467520-99ks/)

## Courses

- [Claude 101 by Anthropic](https://anthropic.skilljar.com/claude-101)
