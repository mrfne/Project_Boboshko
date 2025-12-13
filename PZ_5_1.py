def sum_series(n):

    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Введите количество элементов ряда для суммирования: "))
result = sum_series(n)
print(f"Сумма чисел от 1 до {n} равна {result}")