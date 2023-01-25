def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for x in range(1, num_rows+1):
        for y in range(1, num_columns+1):
            print("%2d" %operation(x, y), end = ' ')
        print()

print_operation_table(lambda x, y: x*y)

"""
Отсчет значений с 1, а не нуля обусловлен тем, что если математическая операция аргументов х и у будет умножение,
то по горизонтали и вертикали появится по одному столбцу с нулевыми значениями.
В случае если математическая операция аргументов х и у будет деление, то будет ошибка, т.к. на 0 делить нельзя.
"""
