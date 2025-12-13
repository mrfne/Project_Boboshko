def swap_pairs():
    while True:
        N = int(input("Введите четное число N (размер списка): "))
        if N % 2 == 0:
            break
        print("N должно быть четным! Попробуйте снова.")
    lst = []
    for i in range(N):
        element = input(f"Введите элемент {i + 1}: ")
        lst.append(element)

    print(f"Исходный список: {lst}")

    for i in range(0, N, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    print(f"Измененный список: {lst}")
    return lst

result3 = swap_pairs()