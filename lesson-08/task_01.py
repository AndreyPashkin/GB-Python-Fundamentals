# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class MyDate:

    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def date_to_int(cls, date_string, period):
        date_array = date_string.split('-')
        if period == 'd':
            return int(date_array[0])
        elif period == 'm':
            return int(date_array[1])
        elif period == 'y':
            return int(date_array[2])
        else:
            return "ошибка ввода данных"

    @staticmethod
    def validate(date_string):
        # переменные, чтобы меньше писать кода:
        day = MyDate.date_to_int(date_string, 'd')
        month = MyDate.date_to_int(date_string, 'm')
        y = MyDate.date_to_int(date_string, 'y')

        print(f'Проверка корректности ввода даты: {date_string}')
        if (month >= 1) and (month <= 12) and (day >= 1) and (day <= 31):
            if month in [1, 3, 5, 7, 8, 10, 12]:
                print('дата корректна')
            elif month in [4, 6, 9, 11] and day <= 30:
                print('дата корректна')
            elif month == 2:  # проверяем количество дней в феврале в зависимости от високосности года
                if ((y % 4 == 0) and (day <= 29) or
                        (y % 4 != 0) and (day <= 28)):
                    print('дата корректна')
                else:
                    print('дата некорректна')

        else:
            print('дата некорректна')


print(MyDate.date_to_int('15-11-2001', 'd'))
print(MyDate.date_to_int('15-11-2001', 'm'))
print(MyDate.date_to_int('15-11-2001', 'y'))

MyDate.validate('15-11-2001')
MyDate.validate('28-02-2001')
MyDate.validate('29-02-2000')
MyDate.validate('29-02-2001')
MyDate.validate('30-02-2000')
