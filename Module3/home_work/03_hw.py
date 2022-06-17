# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []
n = int(input('Введите количество чисел: '))
i = 0
total = 0
while i < n:
    k = random.randint(-100, 100)
    numbers.insert(i, k)
    i += 1
print(numbers)
for number in numbers:
    if (number % 2 == 0 and number > 0):
        total += number
        print(number, end= ',')
    else:
        number += 1
print(' ')
print('Сумма равна =', total)
