def task2():
    print("\n=== Задание 2: Проверка упорядоченности букв ===")

    s = input("Введите строку (цифры и строчные латинские буквы): ")

    if not s:
        print("Ошибка: строка пустая!")
        return

    first_letter_index = -1
    for i, char in enumerate(s):
        if 'a' <= char <= 'z':
            first_letter_index = i
            break

    if first_letter_index == -1:
        print("В строке нет латинских букв. Результат: 0")
        return 0
    for i in range(first_letter_index, len(s) - 1):
        if not ('a' <= s[i] <= 'z'):
            continue

        for j in range(i + 1, len(s)):
            if 'a' <= s[j] <= 'z':
                if s[i] > s[j]:
                    print(f"Порядок нарушен! Первый нарушитель: позиция {j + 1}, символ '{s[j]}'")
                    return j + 1
                break
    print("Все буквы упорядочены по алфавиту. Результат: 0")
    return 0

task2()