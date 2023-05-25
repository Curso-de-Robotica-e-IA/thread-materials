import numpy as np
import threading
from pprint import pprint

def multiply_rows(row, matrix_b, result, row_index):
    # Multiply a row of matrix A with matrix B and store the result in the result matrix
    result[row_index] = np.dot(row, matrix_b)

def multiply_matrices(matrix_a, matrix_b):
    # Create a result matrix with the appropriate dimensions
    result = np.zeros((matrix_a.shape[0], matrix_b.shape[1]))

    # Create a list to store the threads
    threads = []

    # Iterate over the rows of matrix A
    for i in range(matrix_a.shape[0]):
        # Create a thread for each row and start it
        thread = threading.Thread(target=multiply_rows, args=(matrix_a[i], matrix_b, result, i))
        thread.start()
        threads.append(thread)

    pprint(threads)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    return result

# Example usage
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [1, 3, 3], [1, 5, 2], [3, 2, 3], [7, 5, 6], [1, 9, 3], [4, 7, 6], [1, 3, 3], [2, 5, 6]])
matrix_b = np.array([[7, 8], [9, 10], [11, 12]])

result = multiply_matrices(matrix_a, matrix_b)

print(matrix_a)
print(matrix_b)
print(result)
