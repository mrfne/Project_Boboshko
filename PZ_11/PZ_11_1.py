# 1. Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
# полученных последовательностях.

import random
# 1
N = 10
numbers = [random.randint(1, 100) for _ in range(N)]
triples = [x for x in numbers if x % 3 == 0]
others = [x for x in numbers if x % 3 != 0]
print(triples, len(triples))
print(others, len(others))
