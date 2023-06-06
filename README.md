# Thread-materials
Execução assíncrona de comando bloqueantes sem travar a execução da main thread, posibilitando o gerenciamento e delegação de atividades da parte síncrona para a parte assíncrona.

# Contexto de uso
- Aplicações de robótica em tempo real.
    - Processar a decisão e controlar 6 robôs móveis ao mesmo tempo.
- Durante a execução de comandos a biblioteca do robô segura a execução até a movimentação ser concluída.
    - Durante a dispensação a interface e outras operações ficariam travadas.

## Requisitos
- Controlar a execução a partir da main thread;
- Manter a separação de contexto entre as funções e objetos do robô, e da aplicação principal;
- Ser possível pausar e retornar as movimentações do robô de onde parou;
- Ser possível parar a execução e cancelar as movimentações pendentes;
- Limpar erros e reiniciar movimentações.

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

### Constants:
- Padronização de flags, com o uso de enumerações;
- RobotStatus: Status simplificados para a interface de usuário;
- RobotType: Tipo do robô a ser usado, atualmente não utilizado;
- ExecutionStatus: Status completo da execução do provider no gerenciamento do robô e da execução assíncrona;
- ActionCommand: Comandos especiais e de interrupção do robô;
- MoveType: Tipo do sistema de coordenada de movimentação utilizada;

### Packages:
- Pacotes utilizando dataclasses para padronizar o formato dos objetos que contém os parâmetros de comandos para serem executados pelo robô;
- RobotJointCommand: Pacote com os parâmetros que definem uma posição destino para uma movimentação por juntas;
- RobotCartesianCommand: Pacote com os parâmetros que definem uma posição destino para uma movimentação cartesiana;

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
CLI de execução **(robot_provider/run_cli.py)**
```Python
def main():
    robot_controller = RobotCtrl()
    while True:
        tecla = input('Enter a command for using the robot arm: ')
        if tecla == 'c':
            robot_controller.connect()
        elif tecla == 'd':
            robot_controller.disconnect()
        elif tecla == 'mj':
            robot_controller.move([RobotJointCommand(0, 40, 0, 0, 0, 0), RobotJointCommand(0, -40, 0, 0, 0, 0),
                                   RobotJointCommand(30, 40, 0, 0, 0, 0)])
        elif tecla == 'mc':
            robot_controller.move([RobotCartesianCommand(0.2, 0.1, 0.3, 0.0, 0.5, 0.0)])
        elif tecla == 'mz':
            robot_controller.move([RobotJointCommand(0, 0, 0, 0, 0, 0)])
        elif tecla == 's':
            robot_controller.stop()
        elif tecla == 'p':
            robot_controller.pause()
        elif tecla == 'r':
            robot_controller.resume()
        elif tecla == 'g':
            robot_controller.get_status()
        elif tecla == 'q':
            break
```
# Pontos em aberto
- Limpeza de erros;
- Abrir e fechar gripper;
- Obter status da operação direta do robô;
- Parada emergencial;
- Verificação de se o robô está conectado;
- Opção de criação de uso com um robô dammy para testes;
