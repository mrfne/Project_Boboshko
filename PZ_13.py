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