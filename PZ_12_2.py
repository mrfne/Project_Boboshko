# 2. Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.
matrix2 = [[-2, 3, 4], [5, -6, 8], [10, -1, 7]]
even = [x for row in matrix2 for x in row if x > 0 and x % 2 == 0]
print(even, sum(even), sum(even)/len(even) if even else 0)
