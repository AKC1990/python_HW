"""
Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

n = 123
n1 = 123 % 10
n2 = n // 10 % 10
n3 = n // 100
print(n1 + n2 + n3)