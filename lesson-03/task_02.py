# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_user_info(name, surname, birth_year, city, email, phone):
    print(f'{name} {surname}, {birth_year}г.р., {city}, {email}, {phone}')


print('Заполнение информации о пользователе')
user_name = input('Имя: ')
user_surname = input('Фамилия: ')
user_birth_year = input('Год рождения: ')
user_city = input('Место проживания: ')
user_email = input('Email: ')
user_phone = input('Phone: ')

print_user_info(name=user_name,
                surname=user_surname,
                email=user_email,
                phone=user_phone,
                birth_year=user_birth_year,
                city=user_city)
