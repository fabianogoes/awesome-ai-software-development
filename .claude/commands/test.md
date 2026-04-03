# Testar o projeto

Use este comando quando houver mudanças em parsing, geração de HTML ou automações do projeto.

## Passos

1. Rode `python3 -m unittest discover -s src -p 'test*.py' -v`.
2. Revise falhas relacionadas a parsing de tabelas, geração de `index.html` ou automações em `tools/scripts/`.
3. Se a mudança afetar conteúdo renderizado, rode também `python3 src/build.py`.
