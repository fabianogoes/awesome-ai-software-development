---
name: claude-project-setup
description: Cria a estrutura de diretórios e arquivos recomendada para projetos que usam Claude Code. Use esta skill sempre que o usuário pedir para "inicializar projeto Claude", "criar estrutura Claude", "setup Claude project", "preparar projeto para Claude Code", ou qualquer variação de montar a estrutura padrão de um projeto com Claude Code — mesmo que o usuário não mencione explicitamente a palavra "skill". Também ative quando o usuário perguntar "o que preciso criar para usar Claude Code?" ou "como estruturar meu projeto com Claude?".
---

# Claude Project Setup

Esta skill cria a estrutura modular recomendada para projetos que utilizam Claude Code, conforme as boas práticas consolidadas.

## Estrutura alvo

```
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

## Como executar

### 1. Determinar o diretório raiz

Se o usuário não especificou, pergunte ou assuma o diretório de trabalho atual (`pwd`).

### 2. Verificar o que já existe

Antes de criar qualquer coisa, verifique quais itens já existem:

```bash
# Verificar arquivos e diretórios existentes
ls -la
ls -la docs/ 2>/dev/null
ls -la .claude/ 2>/dev/null
ls -la tools/ 2>/dev/null
```

Liste o que foi encontrado e o que está faltando. **Nunca sobrescreva arquivos existentes** — apenas crie os ausentes.

### 3. Criar diretórios ausentes

Crie apenas os diretórios que não existem:

```bash
mkdir -p docs/decisions
mkdir -p docs/runbooks
mkdir -p .claude/commands
mkdir -p .claude/hooks
mkdir -p src
mkdir -p tools/scripts
mkdir -p tools/prompts
mkdir -p images
```

O `mkdir -p` é seguro — não sobrescreve se já existir.

### 4. Criar arquivos ausentes

Verifique cada arquivo antes de criar. Use o conteúdo padrão abaixo.

#### `CLAUDE.md` (se não existir)

```markdown
# CLAUDE.md

Instruções e contexto para o Claude Code neste projeto.

## Visão geral do projeto

[Descreva o projeto aqui]

## Comandos principais

- `[comando de build]`: [descrição]
- `[comando de teste]`: [descrição]
- `[comando de execução]`: [descrição]

## Regras de trabalho

- [Adicione convenções de código, estilo e boas práticas]
- [Adicione restrições importantes]

## Contexto adicional

[Links, decisões importantes, referências]
```

#### `docs/architecture.md` (se não existir)

```markdown
# Arquitetura

Visão geral da arquitetura do projeto.

## Componentes principais

[Descreva os componentes]

## Fluxo de dados

[Descreva o fluxo]

## Dependências externas

[Liste dependências]
```

#### `.claude/settings.json` (se não existir)

```json
{
  "permissions": {}
}
```

### 5. Relatório final

Ao concluir, apresente um resumo claro:

```
✓ Já existiam:
  - CLAUDE.md
  - src/

✓ Criados agora:
  - docs/architecture.md
  - docs/decisions/
  - docs/runbooks/
  - .claude/settings.json
  - .claude/commands/
  - .claude/hooks/
  - tools/scripts/
  - tools/prompts/
  - images/

Estrutura pronta. Próximos passos sugeridos:
1. Preencha o CLAUDE.md com contexto do seu projeto
2. Adicione a arquitetura em docs/architecture.md
3. Configure permissões em .claude/settings.json se necessário
```

## Boas práticas a mencionar ao usuário

Após criar a estrutura, lembre o usuário das boas práticas:

- **`CLAUDE.md`**: mantenha curto, focado e sempre atualizado — é a memória compartilhada do projeto com o Claude.
- **`docs/decisions/`**: registre decisões arquiteturais importantes (ex: `docs/decisions/001-escolha-banco-de-dados.md`).
- **`docs/runbooks/`**: documente procedimentos operacionais recorrentes.
- **`.claude/commands/`**: crie comandos reutilizáveis para tarefas frequentes.
- **`.claude/hooks/`**: use hooks para guardrails e validações automáticas.
- Adapte a estrutura ao tipo real do projeto — evite criar pastas que nunca serão usadas.
