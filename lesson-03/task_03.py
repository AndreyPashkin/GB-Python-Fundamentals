# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# Складываем все элементы списка, и от суммы отнимаем число с минимальным значением
def my_func(a, b, c):
    my_list = [a, b, c]
    return f'Сумма двух наибольших числе: {sum(my_list) - min(my_list)}'


# Получение чисел от пользователя
values = input('Введите три числа через запятую: ')
values = values.split(',')
a_value = float(values[0])
b_value = float(values[1])
c_value = float(values[2])

print(my_func(a_value, b_value, c_value))
