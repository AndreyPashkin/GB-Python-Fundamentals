# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

our_list = input('Введите список элементов (через запятую): ')
our_list = our_list.split(',')
verified_list = []


# Вспомогательные функции
# Проверка на дробное десятичное число
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# тут проверки на тип данных, чтобы они сохранялись в списке, а не были просто строками
# часть проверок пока не получились корректными (list, dict, set)
# и наличие пробелов пока мешается - не успеваю до урока

for item in our_list:
    if item.lower() == 'true':  # Для удобства ввода пользователем - можно ввести в любом регистре
        item = True
    elif item.lower() == 'false':  # Для удобства ввода пользователем - можно ввести в любом регистре
        item = False
    elif item.isdigit():  # Сначала проверяем на целые
        item = int(item)
    elif is_float(item):  # Теперь на дробные
        item = float(item)

    verified_list.append(item)

# Делаем из начального списка два новых списка
# (один с чётными, а второй с нечётными элементами из начального списка)
our_list_1 = verified_list[::2]
our_list_2 = verified_list[1::2]
# Создаём пустой список, в котором будем собирать итоговый список
changed_list = []

# Собираем новый список, переставляя элементы
i = 0
while i < ((len(verified_list) - 1) / 2):
    changed_list.append(our_list_2[i])
    changed_list.append(our_list_1[i])
    i += 1

# Добавляем в новый список последний непарный элемент списка, если он есть
if len(verified_list) % 2 != 0:
    changed_list.append(our_list_1[-1])

# Выводим итоговый список на экран
print(changed_list)