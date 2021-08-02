# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open("my_file.txt", "w",  encoding='utf-8')

print("Вводите строки по одной. Для окончания ввода, на новой строке просто нажмите Enter.")
new_string = input(": ")

while new_string != '':
    my_file.write(new_string + '\n')
    new_string = input(": ")

my_file.close()
