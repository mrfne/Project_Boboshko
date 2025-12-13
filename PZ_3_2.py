summa = float(input("Введите сумму покупки в рублях: "))

if summa < 500:
    discount = 2
elif 500 <= summa < 1000:
    discount = 3
elif 1000 <= summa < 1500:
    discount = 4
elif 1500 <= summa < 2000:
    discount = 5
else:
    discount = 5

discount_amount = summa * discount / 100
final_sum = summa - discount_amount

print(f"Сумма покупки: {summa:.2f} руб.")
print(f"Скидка: {discount}% ({discount_amount:.2f} руб.)")
print(f"Итоговая сумма: {final_sum:.2f} руб.")