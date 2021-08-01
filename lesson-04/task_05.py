# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


my_list = [item for item in range(100, 1000 + 1) if (item % 2 == 0)]

print(reduce(my_func, my_list))
