# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# через list
month_number = int(input('Введите номер месяца: '))
periods = ['зима', 'весна', 'лето', 'осень']

if (month_number <= 2) | (month_number == 12):
    print(f'Это {periods[0]}')
elif (month_number >= 3) & (month_number <= 5):
    print(f'Это {periods[1]}')
elif (month_number >= 6) & (month_number <= 8):
    print(f'Это {periods[2]}')
elif (month_number >= 9) & (month_number <= 11):
    print(f'Это {periods[3]}')

# через dict
month_number = int(input('Введите номер месяца: '))
year_periods = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}

if (month_number <= 2) | (month_number == 12):
    print(f'Это {year_periods.get(1)}')
elif (month_number >= 3) & (month_number <= 5):
    print(f'Это {year_periods.get(2)}')
elif (month_number >= 6) & (month_number <= 8):
    print(f'Это {year_periods.get(3)}')
elif (month_number >= 9) & (month_number <= 11):
    print(f'Это {year_periods.get(4)}')
