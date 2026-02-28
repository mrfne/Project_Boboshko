import math
def TrianglePS(a):

    P = 3 * a
    S = (a ** 2 * math.sqrt(3)) / 4
    return P, S

print("Расчет периметров и площадей трех равносторонних треугольников")

for i in range(3):
    side = float(input(f"Введите длину стороны треугольника {i + 1}: "))
    perimeter, area = TrianglePS(side)

    print(f"Треугольник {i + 1}:")
    print(f"  Сторона: {side}")
    print(f"  Периметр: {perimeter:.2f}")
    print(f"  Площадь: {area:.2f}")
