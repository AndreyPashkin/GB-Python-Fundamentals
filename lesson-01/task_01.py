# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

greetings = 'Здравствуйте,'
proposal = 'Предлагаем Вам, взять кредит в размере'
currency = 'руб.'
name = input('Ваше имя: ')
age = input('Ваш возраст: ')

print(f'{greetings} {name}!')
if int(age) > 18:
    salary = input('Размер вашей зарплаты (руб.): ')
    print(f'{proposal} {int(salary) * 12} {currency}')
else:
    print('Вам кредит брать ещё нельзя')