N = int(input("Введите целое положительное число N: "))

has_digit_two = False
temp = N
while temp > 0:
    digit = temp % 10
    if digit == 2:
        has_digit_two = True
        break
    temp = temp // 10

print(has_digit_two)