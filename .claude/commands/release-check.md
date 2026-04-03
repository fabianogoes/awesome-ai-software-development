# Checklist pré-publicação

Antes de concluir uma alteração:

1. Verifique se os arquivos-fonte corretos foram alterados.
2. Rode `python3 src/build.py` se houve mudança em `README.md`, `CONCEPTS.md` ou `BOOKS.md`.
3. Rode `python3 -m unittest discover -s src -p 'test*.py' -v` se houve mudança em `src/build.py`, arquivos de teste em `src/` ou `tools/scripts/`.
4. Confirme que `index.html` acompanha a versão final do conteúdo.
5. Revise `docs/runbooks/` se o workflow operacional mudou.
