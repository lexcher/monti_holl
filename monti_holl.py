#!/usr/bin/env python3.6
#
# Written by Lexcher, 03.11.2018
# Парадокс Монти Холла
#
import random
num = 10000                                      # количество игр
win = 0                                          # начальное значение выигрышей, которого добьемся, не изменяя выбор
print('Парадокс Монти Холла\n')

for i in range(1, num):
    if random.randint(1, 3) == random.randint(1, 3):
        win += 1  # увеличение выигрышей на 1
win_first_strategy = win * 100 / 10000           # выигрыши по первой стратегии
win_second_strategy = (num - win) * 100 / 10000  # выигрыши по второй стратегии
print(f'Не меняя выбора, выигрыш составляет {win_first_strategy} %')
print(f'Изменяя выбор, выигрыш составляет {win_second_strategy} %')

print('Test')
