# Runbook: Publicar no GitHub Pages

## Pré-condições

- O conteúdo Markdown final está correto.
- `index.html` foi regenerado a partir da versão final das fontes.
- A suíte `python3 -m unittest discover -s src -p 'test*.py' -v` está verde quando houver mudança em parser, testes ou automações.

## Checklist

1. Confirme os arquivos alterados com `git status --short`.
2. Rode `python3 src/build.py` se houve mudança em conteúdo.
3. Rode `python3 -m unittest discover -s src -p 'test*.py' -v` se houve mudança em `src/build.py`, testes em `src/` ou `tools/scripts/`.
4. Verifique se `index.html` está incluído junto da mudança correspondente.
5. Faça o merge no branch publicado pelo Pages.
