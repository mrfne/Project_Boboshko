# 1. В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
# 2. Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.

# Задание 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    matrix[i][i] *= 2
print(matrix)

# Задание 2
matrix2 = [[-2, 3, 4], [5, -6, 8], [10, -1, 7]]
even = [x for row in matrix2 for x in row if x > 0 and x % 2 == 0]
print(even, sum(even), sum(even)/len(even) if even else 0)