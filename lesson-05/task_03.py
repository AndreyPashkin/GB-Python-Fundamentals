# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_file = open("task_03_file.txt", "r", encoding='utf-8')
needToIncrease = []
employeesAmount = 0
salariesAmount = 0

for index, line in enumerate(my_file):
    employeesAmount += 1
    lineData = str(line).split(' ')
    salariesAmount += float(lineData[1])
    if float(lineData[1]) < 20000:
        needToIncrease.append(lineData[0])

print('Зарплата меньше 20 000 рублей у следующих сотрудников: ')
for index, surname in enumerate(needToIncrease):
    print(f'{index + 1}: {surname}')

print(f'Средняя зарплата: {salariesAmount / employeesAmount}')
my_file.close()
