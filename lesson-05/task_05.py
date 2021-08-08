# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_file = open("task_05_file.txt", "r", encoding='utf-8')

numbersLine = my_file.readline()
numbers = numbersLine.split(" ")
numbersAmount = 0

for num in numbers:
    numbersAmount += float(num)

print(numbersAmount)
my_file.close()
