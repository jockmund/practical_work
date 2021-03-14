from random import randint
from sys import maxsize
MAX_N = 53000000
MAX_VALUE = maxsize
MIN_VALUE = -maxsize
# Чтение данных
# print('Как вы хотите считывать информацию?\n1 - ручной ввод, 2 - ввод из файла, 3 - автоматическое тестирование')
# write_mode = int(input())
write_mode = 3

n, array, x = 0, [], 0

# Ввод данных
if write_mode == 1:  # Ввод с клавиатуры
    print('Введите количество элементов')
    n = int(input())
    print('Введите искомый элемент')
    x = int(input())
    print('Введите элементы массива через пробел')
    input_str = input().split(' ')
    array = [int(input_str[i]) for i in range(n)]
elif write_mode == 2:  # Ввод из файла
    with open('data.txt', 'r') as file:
        first_line = file.readline().split(' ')
        n = int(first_line[0])
        x = int(first_line[1])
        second_line = file.readline().split(' ')
        for element in second_line:
            array.append(int(element))
elif write_mode == 3:  # Рандомная генерация
    n = MAX_N
    x = randint(MIN_VALUE, MAX_VALUE)

    def fill_arr(n):
        list_res = []
        for i in range(n):
            list_res.append(randint(MIN_VALUE, MAX_VALUE))
        return list_res

    array = fill_arr(n)

from time import time
# Запуск алгоритма
from linear_search import LinearSearch
linear = LinearSearch(n, array)
start_time = time()
result_index = linear.linear_search(x)
print('Индекс заданного числа в массиве:', result_index, '\n', f'{(time() - start_time) * 1000:.3e}')

from binary_search import BinarySearch
array.sort()
binary = BinarySearch(n, array)
start_time = time()
result_index = binary.binary_search(x)
print('Индекс заданного числа в массиве:', result_index, '\nРезультирующее время:', f'{(time() - start_time) * 1000:.3e}')

from binary_search_1 import BinarySearch_1
binary = BinarySearch_1(n, array)
start_time = time()
result_index = binary.binary_search(x)
print('Индекс заданного числа в массиве:', result_index, '\nРезультирующее время:', f'{(time() - start_time) * 1000:.3e}')