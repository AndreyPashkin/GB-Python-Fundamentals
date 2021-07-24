# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

result: float = 0
one_more: bool = True


def get_sum(numbers, summa):
    numbers_sum = numbers.split(' ')
    for number in numbers_sum:
        if number == 'e':
            global one_more
            one_more = False
            break
        if number != '':  # удаление влияния лишних пробелов в строке
            summa += float(number)
    return summa


numbers_string = input('Введите набор чисел через пробел для получения их суммы:\r\n')
result = get_sum(numbers_string, result)
print(f'Сумма всех введённых чисел: {result}')

while one_more:
    numbers_string = input('Введите набор чисел через пробел для добавления к прежней сумме:\r\n')
    result = get_sum(numbers_string, result)
    print(f'Сумма всех введённых чисел: {result}')
