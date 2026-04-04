# Public Private Structure Design

## Objetivo

Adequar o repositório à estrutura agnóstica proposta para agentes, centralizar comandos e automações sem acoplar o projeto ao Claude, e evoluir o build do GitHub Pages para expor apenas recursos públicos e compartilháveis.

## Decisões principais

### 1. Estrutura canônica de agentes

- `.agents/` será a fonte de verdade para recursos compartilhados entre agentes.
- `.agents/commands/` será o local canônico para comandos.
- `.claude/commands/` deixará de ser origem e passará a existir apenas como compatibilidade.
- `CLAUDE.md` continua como link simbólico para `AGENTS.md`.

### 2. Separação entre público e interno

- `README.md` permanece genérico, orientado ao propósito aberto do repositório.
- `AGENTS.md`, regras internas, scripts operacionais e detalhes de manutenção continuam fora do escopo público por padrão.
- O GitHub Pages deve expor apenas conteúdo útil para a comunidade, nunca detalhes internos de operação do projeto.

### 3. Build público inteligente

- `src/build.py` continuará sendo a fronteira de publicação.
- Além de `README.md`, `CONCEPTS.md` e `BOOKS.md`, o build passará a incluir `CLAUDE_TIPS.md`.
- Também deve suportar novos documentos públicos curados:
  - `docs/purpose.md`
  - `docs/shared-resources.md`
- A UI deve distinguir claramente:
  - catálogo geral do projeto
  - propósito do repositório
  - recursos compartilháveis
  - dicas práticas

### 4. Documentos novos

- `docs/purpose.md`: explica propósito, escopo e princípios do repositório.
- `docs/shared-resources.md`: catálogo público e agnóstico de skills, agents, plugins e convenções compartilháveis.

### 5. Convenção obrigatória

Criar uma rule explícita no projeto estabelecendo:
- novos comandos nascem em `.agents/commands/`
- `.claude/commands/` é compatibilidade, não fonte de verdade

## Impacto esperado

- reduz acoplamento com ferramenta específica
- preserva a proposta aberta e compartilhável do repositório
- melhora a consistência entre documentação, bootstrap e estrutura real
- permite evoluir o GitHub Pages com mais conteúdo útil sem expor operação interna

## Restrições

- manter o build do GitHub Pages funcional
- não expor recursos internos no site público
- preservar conteúdo existente sempre que possível
- migrar com segurança sem perder dados
