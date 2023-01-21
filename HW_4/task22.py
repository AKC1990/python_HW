'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
'''

m = int(input("Введите количество элементов списка 1: "))
n = int(input("Введите количество элементов списка 2: "))

list1 = [int(input(f"Введите число {i+1} списка 1: ")) for i in range(m)]
list2 = [int(input(f"Введите число {i+1} списка 2: ")) for i in range(n)]
result_set = set()

for i in list1:
    if i in list2:
        result_set.add(i)
print(*sorted(result_set))  # Наиболее простое решение. Решение с помощью цикла закомментировано ниже


# result_list = []
# for i in list1:
#     if (i in list2) and (i not in result_list):
#         result_list.append(i)
#         for j in range(len(result_list) - 1):
#             for k in range(len(result_list) - 1):
#                 temp = result_list[k]
#                 if result_list[k] > result_list[k+1]:
#                     result_list[k] = result_list[k+1]
#                     result_list[k+1] = temp
# print(result_list)


