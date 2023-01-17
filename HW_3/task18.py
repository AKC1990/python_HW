'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
'''

n = int(input("Укажите длину массива: "))
x = int(input("Укажите искомое значение: "))
result_list = list()
nearest_index = 0
for i in range(n):
    result_list.insert(i, int(input("Введите число: ")))

print(n)
print(*result_list)
print(x)

if result_list[0] >= x:
    min_variance = result_list[0] - x
else:
    min_variance = x - result_list[0]
for j in range(1, len(result_list)):
    if result_list[j] >= x:
        if min_variance >= result_list[j] - x:
            min_variance = result_list[j] - x
            nearest_index = j
    else:
        if min_variance >= x - result_list[j]:
            min_variance = x - result_list[j]
            nearest_index = j
print(f'-> {result_list[nearest_index]}')