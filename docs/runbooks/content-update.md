# Runbook: Atualizar conteúdo

## Quando usar

Ao editar `README.md`, `CONCEPTS.md` ou `BOOKS.md`.

## Passos

1. Edite apenas o arquivo-fonte correto.
2. Preserve o schema das tabelas esperado pelo parser.
3. Rode `python3 src/build.py`.
4. Revise o diff de `index.html`.
5. Se a mudança tocar parsing ou automação, rode também `python3 -m unittest discover -s src -p 'test*.py' -v`.
