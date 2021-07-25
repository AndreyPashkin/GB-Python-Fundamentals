# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print('Давайте посчитаем успешность работы вашей фирмы')

proceeds = float(input('Введите размер выручки вашей фирмы: '))
costs = float(input('Введите размер издержек вашей фирмы: '))
profitability: float = 0

if proceeds - costs > 0:
    print(f'Вы работаете с прибылью')
    print(f'Рентабельность вашей фирмы: {proceeds / costs}')
    equipment_quantity = int(input('Введите численность сотрудников вашей фирмы: '))
    print(f'Прибыль фирмы в расчёте на одного сотрудника: {(proceeds - costs) / equipment_quantity}')
else:
    print(f'Вы работаете в убыток')