price_per_kg = float(input("Введите цену за 1 кг конфет (в рублях): "))

print("Вес (кг) | Стоимость (руб.)")
print("-" * 25)

for kg in range(1, 11):
    cost = price_per_kg * kg
    print(f"{kg:^9} | {cost:^15.2f}")