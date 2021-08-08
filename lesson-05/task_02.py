# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

my_file = open("task_02_file.txt", "r", encoding='utf-8')
lines_quantity = 0
fileInfo = ''

for index, line in enumerate(my_file):
    lines_quantity += 1
    fileInfo += f'Строка №{index + 1}: слов: {len(line.split(" "))}, символов: {len(line)}\n'

fileInfo += f'Всего строк в файле: {lines_quantity}'
print(fileInfo)
my_file.close()
