# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Автомобиль начал движение"

    def stop(self):
        return "Автомобиль остановился"

    def turn(self, direction):
        return f'Автомобиль поернул {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.speed}'


class TownCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости! Допустимая скорость 60 км/ч. Текущая скорость: {self.speed}'
        else:
            return f'Текущая скорость автомобиля {self.speed}'


class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости! Допустимая скорость 40 км/ч. Текущая скорость: {self.speed}'
        else:
            return f'Текущая скорость автомобиля {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, True)


townCar = TownCar(61, "Синий", "ГАЗ-12345")
sportCar = SportCar(125, "Оранжевый", "ВАЗ-12345")
workCar = WorkCar(42, "Зелёный", "ЩАЗ-12345")
policeCar = PoliceCar(55, "Белый", "УАЗ-12345")

print(f'{townCar.name}: {townCar.show_speed()}')
print(f'{sportCar.name}: {sportCar.show_speed()}')
print(f'{workCar.name}: {workCar.show_speed()}')
print(f'{policeCar.name}: {policeCar.show_speed()}')

print(f'Название: {workCar.name}, цвет: {workCar.color}, скорость: {workCar.speed}, полиция: {workCar.is_police}')

print(f'{workCar.name} - {workCar.go()}')
print(f'{workCar.name} - {workCar.turn("неправо")}')
print(f'{workCar.name} - {workCar.stop()}')
