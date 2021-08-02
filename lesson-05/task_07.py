# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

average_profit = 0
summary_profit = 0
companies_amount = 0
companies_profit = {}
result = []

with open("task_07_file.txt", "r", encoding='utf-8') as my_file:
    for line in my_file:
        temp = line.split(" ")
        companies_amount += 1
        profit = float(temp[2]) - float(temp[3])
        companies_profit.update({temp[0]: profit})
        if profit > 0:
            summary_profit += profit

average_profit = summary_profit / companies_amount
result.append(companies_profit)
result.append({"average_profit": average_profit})

with open("task_07_file.json", "w", encoding='utf-8') as new_file_with_json:
    json.dump(result, new_file_with_json, ensure_ascii=False)
print(f'В файл записана такая информация: \n{result}')
