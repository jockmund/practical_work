from random import randint
from sys import maxsize
MAX_N = 10000000
MAX_VALUE = 10000000
MIN_VALUE = -10000000
# Чтение данных
print('Как вы хотите считывать информацию?\n1 - ручной ввод, 2 - ввод из файла, 3 - автоматическое тестирование')
write_mode = int(input())
print('Какой алгоритм вы хотите использовать?\n1 - линейный поиск, 2 - бинарный поиск')
mode_algorithm = int(input())

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
    array = [randint(MIN_VALUE, MAX_VALUE) for i in range(n)]


from time import time
# Запуск алгоритма
if mode_algorithm == 1:  # Линейный алгоритм
    from linear_search import LinearSearch
    linear = LinearSearch(n, array)
    start_time = time()
    result_index = linear.linear_search(x)
    print('Индекс заданного числа в массиве:', result_index, '\n', f'{(time() - start_time):.3e}')

elif mode_algorithm == 2:  # Бинарный алгоритм
    from binary_search import BinarySearch
    # Сортируем массив для алгоритма
    array.sort()
    print('Отсортированный массив', array)
    binary = BinarySearch(n, array)
    start_time = time()
    result_index = binary.binary_search(x)
    print('Индекс заданного числа в массиве:', result_index, '\nРезультирующее время:', f'{(time() - start_time):.3e}')
