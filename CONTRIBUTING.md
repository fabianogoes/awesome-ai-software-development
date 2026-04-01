# Contribuindo

## Como funciona

Este repositório usa o `README.md`, `CONCEPTS.md` e `BOOKS.md` como **fonte única de verdade**. Um script (`build.py`) lê esses arquivos e gera o `index.html` que alimenta o GitHub Pages.

```
README.md / CONCEPTS.md / BOOKS.md
        │
        ▼
   python3 build.py
        │
        ▼
    index.html (gerado automaticamente)
        │
        ▼
   GitHub Pages (deploy via GitHub Actions)
```

## Editando conteúdo

Edite **apenas** os arquivos Markdown. Nunca edite o `index.html` diretamente — ele é sobrescrito a cada build.

- **Ferramentas, publicações, utilitários, cursos** → `README.md`
- **Conceitos / glossário** → `CONCEPTS.md`
- **Livros** → `BOOKS.md`

### Formato das tabelas

O parser espera tabelas Markdown com estas colunas:

**Ferramentas (CLI, IDE, Frameworks):**
```
| Ferramenta | Descrição | Link | ... |
```

**Skills:**
```
| Skill | Descrição | Link | ... |
```

**Publicações:**
```
| Post | Link |
```

**Utilitários:**
```
| Ferramenta | Descrição | Link |
```

### Sistema de rating (coluna `...`)

| Valor | Significado | Badge na page |
|-------|-------------|---------------|
| `:star::star::star::star::star:` | 5 estrelas | Essencial |
| `:star::star::star:` | 3 estrelas | Recomendado |
| `:star:` | 1 estrela | Novo |
| `:hourglass:` | Ainda não testado | A testar |

### Conceitos (CONCEPTS.md)

Cada conceito segue o formato:

```markdown
### Nome do Termo
Descrição em um parágrafo.
```

Para termos com sigla, use parênteses:

```markdown
### RAG (Retrieval-Augmented Generation)
Descrição...
```

## Testando localmente

```bash
# Gerar o index.html
python3 build.py

# Abrir direto no navegador
open index.html

# Ou via servidor local
python3 -m http.server 3000
# Acesse http://localhost:3000
```

## Deploy

O deploy é **automático**. A cada push no `main` que altere `README.md`, `CONCEPTS.md`, `BOOKS.md` ou `build.py`, o GitHub Actions:

1. Roda `python3 build.py`
2. Publica o resultado no GitHub Pages

### Ativando o GitHub Pages (primeira vez)

1. Vá em **Settings > Pages**
2. Source: **GitHub Actions**
3. Pronto — o workflow `.github/workflows/pages.yml` já está configurado
