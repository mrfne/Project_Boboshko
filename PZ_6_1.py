def arithmetic_progression():
    A = float(input("Введите первый член прогрессии (A): "))
    D = float(input("Введите разность прогрессии (D): "))

    progression = []
    for i in range(10):
        term = A + i * D
        progression.append(term)

    print("Первые 10 членов арифметической прогрессии:")
    for i, term in enumerate(progression, 1):
        print(f"a{i} = {term}")

    return progression

result1 = arithmetic_progression()