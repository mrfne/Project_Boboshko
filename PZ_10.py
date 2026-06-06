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

# Задание 2
with open("text18-3.txt", "r", encoding="windows-1251") as f:
    lines = f.readlines()

print("Содержимое файла:")
for line in lines:
    print(line.rstrip())

punct_count = 0
for i in range(4):
    for ch in lines[i]:
        if ch in string.punctuation:
            punct_count += 1
print(f"\nКоличество знаков пунктуации в первых 4 строках: {punct_count}")

with open("poem_codes.txt", "w", encoding="windows-1251") as f:
    for i, line in enumerate(lines):
        if i == 2:
            f.write(" ".join(str(ord(ch)) for ch in line.rstrip()) + "\n")
        else:
            f.write(line)

print("\nФайл poem_codes.txt создан")