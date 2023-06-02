# Thread-materials

# Contexto de uso
- Aplicações de robótica em tempo real.
    - Processar a decisão e controlar 6 robôs móveis ao mesmo tempo.
- Durante a execução de comandos a biblioteca do robô segura a execução até a movimentação ser concluída.
    - Durante a dispensação a interface e outras operações ficariam travadas.

# Visão geral
## Arquitetura
![Fluxo de dados](/doc/images/provider-fluxo.png)
Gerenciamento de atividades por meio de uma fila de ações. De um lado, temos threads que produzem comandos/requisições, produtoras. Do outro lado, temos threads que consomem os comandos e executam ações, consumidora.
Comunicação encadeada em uma sequência.

![Arquitetura](/doc/images/arquitetura.png)

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
