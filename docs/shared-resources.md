# Recursos Compartilhados

Catálogo público de recursos que podem ser reaproveitados em outros projetos e por diferentes agentes.

## Skills

- `claude-project-setup`: skill para bootstrap de uma estrutura agnóstica de agentes, com foco em `.agents/`, `AGENTS.md` e compatibilidade com ferramentas específicas.

## O que torna uma skill compartilhável

- Resolve um problema recorrente, e não apenas uma necessidade local deste repositório.
- Pode ser reutilizada em outros projetos com pouca ou nenhuma adaptação.
- Explica claramente a convenção que adota, em vez de depender de contexto implícito.
- Evita acoplamento desnecessário a uma única ferramenta quando isso não for estritamente necessário.

## Agents

- `reviewer`: template inicial para revisão com foco em bugs, riscos, regressão e lacunas de teste.

## O que torna um agent compartilhável

- Tem uma responsabilidade clara e limitada.
- Define expectativas de saída, como formato de review, critérios ou guardrails.
- Pode ser adotado por times diferentes sem depender da estrutura interna deste projeto.

## Plugins

- O repositório documenta plugins e integrações úteis no catálogo principal.
- Recursos compartilhados devem evitar dependência exclusiva de uma ferramenta.
- Sempre que um plugin exigir convenções próprias, isso deve ser documentado de forma explícita.

## Convenções

- `.agents/` é a fonte de verdade para recursos compartilhados entre agentes.
- `AGENTS.md` é o contexto global compartilhado.
- `.claude/` e `CLAUDE.md` existem como compatibilidade.
- `.agents/commands/` é a origem canônica dos comandos.
- `.claude/commands/` permanece como wrapper mínimo de compatibilidade.
- Recursos promovidos a padrão do projeto devem ser descritos aqui antes de entrarem no setup padrão.

## Instalar a skill de setup

Há duas formas principais de adotar a estrutura-base deste projeto em outro repositório.

### Via scripts do projeto

- Linux/macOS: `bash scripts/setup-agents.sh full`
- Windows CMD: `scripts\setup-agents.cmd full`
- Windows PowerShell: `powershell -ExecutionPolicy Bypass -File .\scripts\setup-agents.ps1 -Profile full`

### Via adaptação manual

- Crie `.agents/` como fonte de verdade para commands, skills, agents e rules.
- Use `AGENTS.md` como contexto global compartilhado.
- Trate `CLAUDE.md` e `.claude/` como camadas de compatibilidade.
- Mantenha a documentação pública separada dos artefatos operacionais internos.

### O que o setup cria

- Estrutura base em `.agents/`.
- `AGENTS.md` com contexto inicial.
- Aliases de compatibilidade para Claude.
- Templates públicos e operacionais do perfil `full`.

## Quando promover algo para este catálogo

- Quando o recurso puder ser reaproveitado por outros projetos.
- Quando ele expressar uma convenção agnóstica, e não apenas um detalhe interno.
- Quando houver valor em documentar instalação, uso ou expectativas de manutenção.
