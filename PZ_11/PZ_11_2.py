# Задание 2. Составить генератор (yield), который выводит из строки только цифры
def digits(s):
    for ch in s:
        if ch.isdigit():
            yield ch

s = "апельсины 45 991 63 100 12 яблоки 13 47 26 0 16"
print(list(digits(s)))
