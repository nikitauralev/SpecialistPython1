# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint

import random
numbers = []
n = int(input('Введите количество чисел: '))
i = 0
while i < n:
    k = random.randint(-100, 100)
    numbers.insert(i, k)
    i += 1
print(numbers)
