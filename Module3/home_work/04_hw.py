# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

import random
import math
numbers = [9, 6, 100, 4, 3]
lists = []
# n = int(input('Введите количество чисел: '))
i = 0
total = 0
# while i < n:
#     k = random.randint(-100, 100)
#     numbers.insert(i, k)
#     i += 1
for number in numbers:
    if (number > 0):
        x = math.sqrt(number)
        total += x
        #print(total)
        if (x == int(x)):
            lists.append(int(x))
    else:
        print('')
print('Начальный список: ', numbers)
print('Конечный список: ', lists)
