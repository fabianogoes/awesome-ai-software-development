# Arquitetura do Projeto

## Visão geral

Este repositório publica uma coleção curada de referências sobre desenvolvimento de software com IA. A arquitetura é intencionalmente simples: arquivos Markdown na raiz servem como fonte de verdade, um script Python converte esse conteúdo para HTML estático, e o GitHub Pages publica o resultado.

## Fluxo de dados

```text
README.md / CONCEPTS.md / BOOKS.md
              |
              v
       python3 src/build.py
              |
              v
          index.html
              |
              v
        GitHub Pages
```

## Componentes principais

- `README.md`: catálogo principal de ferramentas, publicações, utilitários e cursos.
- `CONCEPTS.md`: glossário de conceitos.
- `BOOKS.md`: lista de livros.
- `src/build.py`: parser e gerador de `index.html`.
- `src/test_build.py`: testes do fluxo principal de parsing e geração.
- `src/test_claude_post_edit_check.py`: testes da automação compartilhada do Claude Code.
- `.claude/`: comandos e hooks compartilhados para uso com Claude Code.
- `tools/scripts/`: scripts utilitários usados por hooks e workflows operacionais.
- `docs/`: documentação de arquitetura, decisões e runbooks.

## Restrições importantes

- `index.html` é artefato gerado, não fonte de verdade.
- O parser depende dos cabeçalhos atuais das tabelas Markdown.
- Mudanças em automações devem evitar efeitos colaterais destrutivos.
