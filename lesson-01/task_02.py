# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

# Вариант 1
timeInSeconds = input('Введите время в секундах:')

hours = int(timeInSeconds) // 3600
minutes = (int(timeInSeconds) - 3600 * (int(timeInSeconds) // 3600)) // 60
seconds = int(timeInSeconds) % 60

if hours < 10:
    hours = '0' + str(hours)

if minutes < 10:
    minutes = '0' + str(minutes)

if seconds < 10:
    seconds = '0' + str(seconds)

print(f'{hours}:{minutes}:{seconds}')

# Вариант 2: С использованием спецификаторов формата 'd' и '%':
timeInSeconds = input('Введите ещё раз время в секундах:')

hours = int(timeInSeconds) // 3600
minutes = (int(timeInSeconds) - 3600 * (int(timeInSeconds) // 3600)) // 60
seconds = int(timeInSeconds) % 60

print('%02d:%02d:%02d' % (hours, minutes, seconds))
