# Thread-materials

# Contexto de uso

# Visão geral
## Arquitetura


## Especificação de elementos:
### Robot Execution Context:
- Contexto compartilhado entre as threads, memória compartilhada;
- Passagem de dados e mensagem entre as threads;
- Singleton para garantir a unicidade do objeto;
- Embrulho com mutex para gerenciar os acessos, com o uso de gets e sets;

### Robot Provider:
- Contexto com os objetos do robô, a conexão e o threadPool;
- Criação e submissão de tarefas para a execução no threadPool;
- Interface entre a chamada síncrona e a assíncrona;

### Robot Controller:
- Gerencia as regras de negócio de manipulação do robot provider;
- Escreve valores no contexto compartilhado com o robô e dispara a execução;

### ThreadPool:
- Recebe as tasks e seus contextos;
- Cria e controla o ciclo de vidas as threads associadas;

### Tasks:
- Operação de conexão;
- Operação de desconexão;
- Operação de Flush de erros;
- Execução de uma sequência de comandos;

# Exemplo de uso

# Pontos em aberto
