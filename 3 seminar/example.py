import numpy as np

# Создаём вектор из 10 значений
a1 = np.arange(10)
print("Исходный вектор: ", a1)

# Преобразуем вектор в матрицу размером 5x2
matrix = np.reshape(a1, (5, 2))
print("Матрица размером 5x2: ")
print(matrix)