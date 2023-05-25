import threading
import numpy as np

# Variáveis compartilhadas entre as threads
result1 = None
result2 = None
lock = threading.Lock()

# Função que será executada em uma thread
def thread_function(name):
    global result1, result2
    
    print("Thread", name, "iniciada.")
    
    # Operação complexa com numpy
    matrix = np.random.rand(2, 2)  # Cria uma matriz 1000x1000 de valores aleatórios
    result = np.dot(matrix, matrix)  # Realiza o produto de matrizes
    
    with lock:
        if name == 1:
            result1 = result
        elif name == 2:
            result2 = result
    
    print("Thread", name, "finalizada.")

# Criação das threads
thread1 = threading.Thread(target=thread_function, args=(1,))
thread2 = threading.Thread(target=thread_function, args=(2,))

# Inicia as threads
thread1.start()
thread2.start()

# Aguarda até que ambas as threads terminem
thread1.join()
thread2.join()

print("Resultados:")
print("Thread 1:\n", result1)
print("Thread 2:\n", result2)
print("Programa finalizado.")