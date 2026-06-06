# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
# корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
# 86532547891), а во второй с некорректными номерами телефонов. Посчитать
# полученные строки в каждом файле.
import re

with open("hotline.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

correct = [line for line in lines if re.search(r'\d{11}', line)]
incorrect = [line for line in lines if not re.search(r'\d{11}', line)]

with open("correct_phones.txt", "w", encoding="utf-8") as f:
    f.writelines(correct)

with open("incorrect_phones.txt", "w", encoding="utf-8") as f:
    f.writelines(incorrect)

print(f"Корректных: {len(correct)}")
print(f"Некорректных: {len(incorrect)}")
