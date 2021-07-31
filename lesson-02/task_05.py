# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
nextStep = True

print('Для выхода из системы ввода рейтингов, введите любое значение, кроме целого числа.')
print(f'Текущий список рейтингов: {my_list}')

while nextStep:
    new_value = input('Введите ещё одно значение рейтинга: ')
    # с использованием sort():
    # if new_value.isdigit():
    #     my_list.append(int(new_value))
    #     my_list.sort()
    #     my_list.reverse()
    #     print(my_list)

    # без использования sort():
    if new_value.isdigit():
        new_value = int(new_value)
        inserted: bool = False
        for index, item in enumerate(my_list):
            if new_value > item:
                my_list.insert(index, new_value)
                inserted = True
                break

        if not inserted:
            my_list.append(new_value)

        print(my_list)
    else:
        print(f'Спасибо за использование нашей системы рейтингов! \r\nИтоговый результат: {my_list}')
        nextStep = False