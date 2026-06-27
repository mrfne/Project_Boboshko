#2. Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы третей
# строки их числовыми кодами.
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
