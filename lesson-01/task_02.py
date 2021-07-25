# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

# Вариант 1
timeInSeconds = int(input('Введите время в секундах:'))

hours = timeInSeconds // 3600
minutes = (timeInSeconds - 3600 * (timeInSeconds // 3600)) // 60
seconds = timeInSeconds % 60

if hours < 10:
    hours = '0' + str(hours)

if minutes < 10:
    minutes = '0' + str(minutes)

if seconds < 10:
    seconds = '0' + str(seconds)

print(f'{hours}:{minutes}:{seconds}')

# Вариант 2: С использованием спецификаторов формата 'd' и '%':
timeInSeconds = int(input('Введите ещё раз время в секундах:'))

hours = timeInSeconds // 3600
minutes = (timeInSeconds - 3600 * (timeInSeconds // 3600)) // 60
seconds = timeInSeconds % 60

print('%02d:%02d:%02d' % (hours, minutes, seconds))
