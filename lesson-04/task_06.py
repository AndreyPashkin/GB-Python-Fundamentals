# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count
from itertools import cycle

# пункт а:

# С какого числа генерируем:
start = 10
end = 20

# Сколько надо сгенерировать:
n = 5

for item in count(start):
    if item > end:
        break
    else:
        print(item)

# пробел между заданиями в выводе
print('\r\n')

# пункт б:
start_list = [1, 2, 5, 4, 3, 11, 21, 123, 12, 0, 8]

for item in cycle(start_list):
    if item > 100:
        break
    print(item)
