# Concepts

### Chat
Interface conversacional com um modelo de IA. No desenvolvimento de software, é usada para explorar soluções, gerar código, revisar PRs e debugar — funcionando como um par de programação sempre disponível.

### Prompt
Instrução ou entrada que você envia ao modelo. É o principal mecanismo de controle do desenvolvedor: a qualidade do output depende diretamente da clareza e especificidade do prompt. Inclui contexto, exemplos, restrições e o objetivo desejado.

### Token
Unidade básica de processamento de texto em LLMs — aproximadamente 4 caracteres ou ¾ de uma palavra em inglês. Impacta diretamente o custo (cobrança por token) e os limites de entrada/saída. Código é mais "denso" em tokens que texto comum.

### Context
A "janela de memória" do modelo — tudo que ele pode ver durante uma conversa: histórico de mensagens, arquivos carregados, resultados de ferramentas. Quanto maior o contexto, mais caro e lento. Gerenciar bem o contexto (o que incluir, o que descartar) é essencial para eficiência.

### Model
A rede neural treinada que processa prompts e gera respostas. Escolher o modelo certo é um trade-off entre capacidade, velocidade e custo: modelos menores (Haiku) para tarefas simples e rápidas; modelos maiores (Opus/Sonnet) para raciocínio complexo e arquitetura.

### MCP
Model Context Protocol — padrão aberto da Anthropic para conectar modelos de IA a ferramentas e fontes de dados externas (bancos de dados, APIs, sistemas de arquivos). Permite que o agente execute ações reais no ambiente do desenvolvedor de forma padronizada.

### Skill
Instrução reutilizável que orienta o modelo a seguir um processo específico — como um SOP (procedimento operacional padrão) para o AI. No Claude Code, skills definem workflows (TDD, debugging, code review) garantindo consistência entre sessões.

### Plugin
Extensão que adiciona capacidades a ferramentas de AI. No Claude Code, um plugin pode incluir skills, hooks, comandos e servidores MCP, empacotados e compartilháveis entre times — equivalente a um pacote npm, mas para comportamentos de AI.

### Agent
Sistema de IA que opera de forma autônoma, tomando decisões e executando ações em sequência para atingir um objetivo. No desenvolvimento de software, agentes podem planejar, escrever código, rodar testes e corrigir bugs com mínima intervenção humana.

### RAG (Retrieval-Augmented Generation)
Técnica que combina busca em bases de conhecimento externas com geração de texto por LLMs. Em vez de depender apenas do treinamento do modelo, o RAG recupera documentos relevantes e os usa como contexto, melhorando precisão e reduzindo alucinações.

### Tool Use / Function Calling
Capacidade do modelo de invocar ferramentas externas (APIs, funções, comandos) durante a geração de resposta. Permite que o modelo execute ações reais — buscar dados, rodar código, acessar sistemas — em vez de apenas gerar texto.
