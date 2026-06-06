# 1. Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
# полученных последовательностях.
# 2. Составить генератор (yield), который выводит из строки только цифры

import random
# 1
N = 10
numbers = [random.randint(1, 100) for _ in range(N)]
triples = [x for x in numbers if x % 3 == 0]
others = [x for x in numbers if x % 3 != 0]
print(triples, len(triples))
print(others, len(others))

# 2
def digits(s):
    for ch in s:
        if ch.isdigit():
            yield ch

s = "апельсины 45 991 63 100 12 яблоки 13 47 26 0 16"
print(list(digits(s)))