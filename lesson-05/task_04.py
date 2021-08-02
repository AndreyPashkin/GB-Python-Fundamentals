# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_file = open("task_04_file.txt", "r", encoding='utf-8')
my_file_rus = open("task_04_file_rus.txt", "w", encoding='utf-8')


def translate(word):
    if word == 'One':
        return 'Один'
    elif word == 'Two':
        return 'Два'
    elif word == 'Three':
        return 'Три'
    elif word == 'Four':
        return 'Четыре'


for line in my_file:
    line_list = line.split(" — ")
    my_file_rus.write(f'{translate(line_list[0])} - {line_list[1]}')

my_file.close()
my_file_rus.close()
