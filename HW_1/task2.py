"""
Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

n = int(input("Введите трехзначное число: "))
while True:
    if 100 <= n <= 999:
        n1 = n // 100
        n2 = n // 10 % 10
        n3 = n % 10
        print(f' {n1 + n2 + n3} ({n1} + {n2} + {n3})')
        break
    else:
        print("Некорректное значение.")
        n = int(input("Введите трехзначное число: "))
