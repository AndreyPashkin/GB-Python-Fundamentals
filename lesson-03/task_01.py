# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

dividend = float(input('Введите значение делимого: '))
divider = float(input('Введите значение делителя: '))

while divider == 0:
    divider = float(input('Делить на ноль нельзя. Введите другое значение делителя: '))


def division(dividend_value, divider_value):
    return dividend_value / divider_value


print(f'Результат: {division(dividend, divider)}')
