# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Квадраты четных элементов:
# Сумма квадратов четных элементов:
# Среднее арифметическое суммы квадратов четных элементов:
import random
import string

# Задание 1
nums = [random.randint(-20, 20) for _ in range(10)]
with open("numbers.txt", "w") as f:
    f.write(" ".join(map(str, nums)))

with open("numbers.txt", "r") as f:
    data = list(map(int, f.read().split()))

even_squares = [x*x for x in data if x % 2 == 0]

with open("result.txt", "w") as f:
    f.write(f"Исходные данные: {data}\n")
    f.write(f"Количество элементов: {len(data)}\n")
    f.write(f"Минимальный элемент: {min(data)}\n")
    f.write(f"Квадраты четных элементов: {even_squares}\n")
    f.write(f"Сумма квадратов четных элементов: {sum(even_squares)}\n")
    f.write(f"Среднее арифметическое: {sum(even_squares)/len(even_squares) if even_squares else 0}\n")
