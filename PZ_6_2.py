def find_first_local_minimum():
    N = int(input("Введите размер списка N: "))

    lst = []
    for i in range(N):
        element = float(input(f"Введите элемент {i + 1}: "))
        lst.append(element)

    print(f"Ваш список: {lst}")

    index = -1

    if N > 1 and lst[0] < lst[1]:
        index = 0
    elif N > 2:
        for i in range(1, N - 1):
            if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
                index = i
                break
        if index == -1 and N > 1 and lst[N - 1] < lst[N - 2]:
            index = N - 1

    if index != -1:
        print(f"Первый локальный минимум: элемент {index + 1} = {lst[index]}")
        print(f"Индекс: {index} (в программировании счёт с 0)")
    else:
        print("Локальный минимум не найден")

    return index

result2 = find_first_local_minimum()