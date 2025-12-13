def task1():
    print("=== Задание 1: Соседние символы ===")

    C = input("Введите символ: ")

    if len(C) != 1:
        print("Ошибка: нужно ввести ровно один символ!")
        return

    code = ord(C)

    prev_char = chr(code - 1)
    next_char = chr(code + 1)

    print(f"Символ: '{C}' (код: {code})")
    print(f"Предыдущий символ: '{prev_char}' (код: {code - 1})")
    print(f"Следующий символ: '{next_char}' (код: {code + 1})")

    return prev_char, next_char

task1()