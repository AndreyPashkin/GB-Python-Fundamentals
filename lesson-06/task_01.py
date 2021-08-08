# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    colors = ["красный", "жёлтый", "зелёный"]

    def __init__(self):
        self.__color = TrafficLight.colors[0]

    def running(self, color0_time: int, color1_time: int, color2_time: int):
        while True:
            self.__color = TrafficLight.colors[0]
            print(self.__color)
            time.sleep(color0_time)
            self.__color = TrafficLight.colors[1]
            print(self.__color)
            time.sleep(color1_time)
            self.__color = TrafficLight.colors[2]
            print(self.__color)
            time.sleep(color2_time)


t = TrafficLight()
t.running(7, 2, 7)
