# Rebuild do site

Use este comando quando houver mudanças em conteúdo ou estrutura que impactem a página gerada.

## Passos

1. Rode `python3 src/build.py`.
2. Confirme que `index.html` foi atualizado sem erro.
3. Se houve mudança em `src/build.py` ou testes, rode também `python3 -m unittest discover -s src -p 'test*.py' -v`.
