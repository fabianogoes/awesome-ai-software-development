<p align="center">
    <img src="images/claude-jumping.svg" alt="Claude Code mascot jumping" width="120" height="100">
</p>

<h1 align="center">Awesome AI Software Development</h1>

<p align="center">
  Uma lista curada de ferramentas, frameworks, conceitos e referências<br>
  para quem usa Inteligência Artificial no desenvolvimento de software.
</p>

<p align="center">
  <a href="https://fabianogoes.github.io/awesome-ai-software-development/">
    <img src="https://img.shields.io/badge/Web-GitHub%20Pages-E07C4C?style=for-the-badge" alt="GitHub Pages">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
  </a>
</p>

Este repositório reúne referências, ferramentas e recursos compartilháveis para quem quer entender melhor como IA está mudando a forma de projetar, construir e evoluir software.

## Tabela de contexto

- [x] [Ferramentas](#ferramentas) - CLI agents, IDEs, frameworks, MCPs, plugins e skills para desenvolvimento com IA
- [x] [Publicações](#publicações) - Artigos e vídeos sobre práticas e técnicas
- [x] [Utilitários](#utilitários) - Referências, templates e guias de metodologia
- [x] [Cursos](#cursos) - Cursos online sobre IA para desenvolvedores
- [x] [Outros](#outros) - Conceitos, livros e dicas complementares

---

## Ferramentas

### CLI

Agentes de coding no terminal — pair programming com IA direto no seu workflow.

| Ferramenta  | Descrição                                                                                  | Link                                                        | Avaliação                      |
| ----------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------ |
| Claude Code | Agente de coding da Anthropic, profundo entendimento de codebases e contexto longo         | [code.claude.com](https://code.claude.com/docs/pt/overview) | :star::star::star::star::star: |
| Codex       | Ferramenta de coding da OpenAI, geração e edição de código via CLI                         | [openai.com](https://openai.com/pt-BR/codex/)               | :star::star::star:             |
| Gemini CLI  | CLI open-source do Google com integração ao Gemini e Google Search                         | [geminicli.com](https://geminicli.com/)                     | :star:                         |
| Aider       | Pair programming no terminal, integra com Git local, suporta Claude/GPT/Ollama             | [aider.chat](https://aider.chat/)                           | :hourglass:                    |
| OpenCode    | Alternativa open-source ao Claude Code, suporta praticamente todos os provedores de modelo | [github.com/sst/opencode](https://github.com/sst/opencode)  | :hourglass:                    |

### IDE

IDEs com IA integrada ao fluxo de edição.

| Ferramenta               | Descrição                                                                                           | Link                             | Avaliação         |
| ------------------------ | --------------------------------------------------------------------------------------------------- | ---------------------------------| ------------------ |
| Cursor                   | IDE com IA nativa integrada ao fluxo de edição                                                      | https://cursor.com/              | :hourglass:        |
| Antigravity              | IDE da Google com agente de coding agentico avançado                                                | https://antigravity.google/      | :star:             |
| Windsurf                 | IDE com agente "Cascade" (modos Write, Chat e Turbo), concorrente direto ao Cursor                  | https://windsurf.com/            | :hourglass:        |
| Zed                      | Editor open-source em Rust, extremamente rápido, suporta Claude, Gemini e modelos locais via Ollama | https://zed.dev/                 | :hourglass:        |
| VS Code + GitHub Copilot | O VS Code com Copilot nativo e ecossistema de extensões de IA (Continue, Codeium, RooCode)          | https://code.visualstudio.com/   | :star::star::star: |
| Trae                     | IDE gratuita da ByteDance, construída sobre VS Code, com agentes de IA integrados (GPT-4 e Claude)  | https://www.trae.ai/             | :star:             |

### Frameworks/Bibliotecas

Frameworks e libs que potencializam o desenvolvimento com agentes de IA.

| Ferramenta                   | Descrição                                                                        | Link                                                        | Avaliação                      |
| ---------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------ |
| GSD - GET SHIT DONE          | Framework para automação de tarefas de desenvolvimento com IA                    | https://github.com/gsd-build/get-shit-done                  | :star:                         |
| OpenSpec                     | Framework de especificação orientado a IA                                        | https://github.com/Fission-AI/OpenSpec                      | :star::star::star:             |
| SpecKit                      | Guia e kit para spec-driven development no GitHub                                | https://github.com/github/spec-kit/blob/main/spec-driven.md | :hourglass:                    |
| Superpowers                  | Extensões e superpoderes para agentes de IA                                      | https://github.com/obra/superpowers                         | :star::star::star::star::star: |
| Agent OS                     | Framework para construir e orquestrar agentes de IA com fluxos reproduzíveis     | https://buildermethods.com/agent-os                          | :hourglass:                    |
| QMD - Query Markup Documents | Documentos interativos com queries para IA                                       | https://github.com/tobi/qmd                                 | :star::star::star:             |
| ccusage                      | Analisador de uso e custo do Claude Code                                         | https://github.com/ryoppippi/ccusage                        | :star::star::star:             |
| OpenRouter                   | Gateway unificado para 300+ modelos de IA via API compatível com OpenAI          | https://openrouter.ai                                       | :star::star::star::star:       |

### MCP

Servidores MCP e integrações para conectar AI coding tools a serviços externos e automações.

| MCP                | Descrição                                                                                                                     | Link                                                                  | Avaliação   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------- |
| Grafana MCP Server | Servidor MCP para acessar instâncias Grafana e o ecossistema ao redor                                                        | https://github.com/grafana/mcp-grafana                                | :hourglass: |
| Playwright MCP     | Servidor MCP de automação de navegador e testes E2E com Playwright, permitindo interações via snapshots de acessibilidade   | https://github.com/microsoft/playwright-mcp                           | :hourglass: |
| Netlify MCP Server | Servidor MCP da Netlify para build, deploy e operações relacionadas                                                          | https://docs.netlify.com/build/build-with-ai/netlify-mcp-server/      | :hourglass: |

### Plugins

Plugins instaláveis que estendem AI coding tools com capacidades adicionais.

| Plugin          | Descrição                                              | Link                                                                        | Avaliação                      |
| --------------- | ------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------ |
| Frontend Design | Plugin para design e geração de frontend no Claude Code | https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design | :star::star::star::star::star: |
| Codex for Claude Code | Plugin da OpenAI que integra o Codex ao Claude Code | https://github.com/openai/codex-plugin-cc                                   | :hourglass:                    |
| Firecrawl       | Plugin para o Claude Code que permite rastrear e extrair conteúdo da web para alimentar fluxos de trabalho e agentes        | https://www.firecrawl.dev/integrations/claude-code                         | :hourglass:                    |

### Skills

Skills e coleções de agentes para Claude Code e outros AI coding tools.

| Skill            | Descrição                                                                                                                     | Link                                                                        | Avaliação                      |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------ |
| Interface Design | Skill para design de interface                                                                                                | https://github.com/Dammyjay93/interface-design                              | :star::star::star::star::star: |
| Napkin           | Uma habilidade de Claude Code que dá ao agente uma memória persistente de seus erros                                          | https://github.com/blader/napkin                                            | :star:                         |
| TLC Spec Driven  | Tech Leads Club - Skill para desenvolvimento orientado a especificações com agentes de IA                                     | https://agent-skills.techleads.club/skills/tlc-spec-driven/                 | :hourglass:                    |

#### Repositórios de Skills

Coleções e repositórios com múltiplas skills prontas para uso.

- [anthropics/skills](https://github.com/anthropics/skills) — Repositório oficial da Anthropic com skills para Claude Code
- [Agent Skills](https://agent-skills.techleads.club/skills/) — Tech Leads Club - coleção de skills para agentes de IA :star::star::star::star::star:
- [Agency Agents](https://github.com/msitarzewski/agency-agents) — Coleção de personalidades de agentes de IA, nascida de meses de iteração da comunidade :star::star::star:
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — Coleção curada de skills para Claude
- [claude-code-templates](https://github.com/davila7/claude-code-templates) — Coleção de templates prontos para Claude Code, disponível também em [aitmpl.com](https://www.aitmpl.com)

---

## Publicações

### Write

Artigos, guias e referências escritas sobre desenvolvimento com IA.

| Post                                                                   | Link                                                                     |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 10 Claude Code tips from Boris, the creator of Claude Code, summarized | https://ykdojo.github.io/claude-code-tips/content/boris-claude-code-tips |
| Melhores práticas para Claude Code                                     | https://code.claude.com/docs/pt/best-practices                           |
| Building effective agents                                              | https://www.anthropic.com/engineering/building-effective-agents           |
| Prompt Engineering Guide                                               | https://platform.openai.com/docs/guides/prompt-engineering               |
| Gemini API Cookbook                                                     | https://github.com/google-gemini/cookbook                                 |
| claude-code-best-practice - practice makes claude perfect              | https://github.com/shanraisshan/claude-code-best-practice                |
| Awesome Claude                                                         | https://awesomeclaude.ai/                                                |
| RALPH WIGGUM AI LOOP TECHNIQUE                                         | https://awesomeclaude.ai/ralph-wiggum                                    |
| Anatomy of the .claude/ folder                                         | https://x.com/akshay_pachaar/status/2035341800739877091                  |
| Estrutura de Projeto Claude Code - 10 insights por Lucíola Coelho      | https://www.linkedin.com/posts/luciola-coelho-agencia-de-ia_claudemd-share-7441180082175467520-99ks/ |

### Video

Videos sobre workflows, boas práticas e casos reais de uso.

| Post                                                                                      | Link                                               |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Como eu uso o Claude Code (Workflow Anti-Vibe Coding)                                     | https://youtu.be/BcLtqQ3JlMU?si=eDx2dRt-ZbAx3DGc  |
| Claude Code best practices \| Code w/ Claude                                              | https://www.youtube.com/watch?v=T-fJQHxWTAs        |
| Como a Stripe criou agentes de IA que escrevem mais de 1.000 solicitações de pull por semana | https://youtu.be/GQ6piqfwr5c?si=ZUYW7CDnR07FcOgB |
| Google Antigravity SEM LIMITES: como usar IA grátis sem travar                               | https://youtu.be/mx_K2qAFz5w?si=VuXAId0B4e9yGhUS  |

---

## Utilitários

Metodologias, templates e referências para estruturar o trabalho com IA.

| Ferramenta                                         | Descrição                                                | Link                                                                  |
| -------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| Spec-Driven Development: Kiro, spec-kit, and Tessl | Artigo do Martin Fowler explorando ferramentas de SDD    | <https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html> |
| Architecture Decision Record (ADR)                 | Templates e guias para registrar decisões de arquitetura | <https://github.com/joelparkerhenderson/architecture-decision-record> |
| CLAUDE.md Guide                                    | Guia oficial da Anthropic para configurar memory files   | <https://code.claude.com/docs/en/memory>                              |

## Cursos

- [Claude 101 - Anthropic Academy](https://anthropic.skilljar.com/claude-101)
- [Curso de Inteligência Artificial para Devs (Nova Versão) com Rodrigo Branas e Pedro Nauck](https://branas.io/cursos/inteligencia-artificial-para-devs/?utm_source=campaign1)
- [Claude Code: A Highly Agentic Coding Assistant by DeepLearning.ai](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)
- [Gemini CLI: Code & Create with an Open-Source Agent by DeepLearning.ai](https://www.deeplearning.ai/short-courses/gemini-cli-code-and-create-with-an-open-source-agent/)

## Outros

- [Propósito](docs/purpose.md) — O que este projeto quer ser, o que busca fazer e o que evita
- [Recursos Compartilhados](docs/shared-resources.md) — Skills, agents, plugins e convenções que podem ser reutilizados em outros projetos
- [AI Concepts](CONCEPTS.md) — Glossário de termos essenciais (Chat, Prompt, Token, MCP, Agent...)
- [Books](BOOKS.md) — Livros recomendados sobre IA e desenvolvimento
- [Claude Tips](CLAUDE_TIPS.md) — Dicas e referências rápidas para Claude Code

---

## Contribuindo

Este repositório é aberto à comunidade! Se você conhece uma ferramenta, conceito, vídeo ou recurso que deveria estar aqui, fique à vontade para contribuir:

1. Faça um **fork** do repositório: [fabianogoes/awesome-ai-software-development](https://github.com/fabianogoes/awesome-ai-software-development)
2. Adicione o conteúdo na seção apropriada do `README.md`
3. Abra um **Pull Request** com uma breve descrição do que foi adicionado

Toda contribuição é bem-vinda, seja uma nova ferramenta, um link útil, uma correção ou uma sugestão de melhoria.

---

<p align="center">
  <img src="images/MIT.png" height="50" width="150">
</p>
