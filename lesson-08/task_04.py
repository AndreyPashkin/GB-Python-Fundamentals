# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

import json


class Equipment:
    def __init__(self, equipment_id, name, price):
        self.equipment_id = equipment_id
        self.name = name
        self.price = price


class Printer(Equipment):
    def __init__(self, equipment_id, name, price, printer_type):
        super().__init__(equipment_id, name, price)
        self.printer_type = printer_type

    def __str__(self):
        return f'Название принтера: {self.name}; \nЦена: {self.price} руб.; \nТип принтера {self.printer_type}\n'


class Scanner(Equipment):
    def __init__(self, equipment_id, name, price, scanner_type):
        super().__init__(equipment_id, name, price)
        self.scanner_type = scanner_type

    def __str__(self):
        return f'Название сканера: {self.name}; \nЦена: {self.price}; \nТип сканера {self.scanner_type}\n'


class Xerox(Equipment):
    def __init__(self, equipment_id, name, price, xerox_type):
        super().__init__(equipment_id, name, price)
        self.xerox_type = xerox_type

    def __str__(self):
        return f'Название копира: {self.name}; \nЦена: {self.price}; \nТип копира {self.xerox_type}\n'


# тестирование создания записей об оборудовании
p1 = Printer("001", "Epson-12345", 12345, "Струйный")
print(p1)

s1 = Scanner("002", "Epson-5432", 5432, "Планшетный")
print(s1)

x1 = Xerox("003", "Xerox-21345", 21345, "Цифровой")
print(x1)


class Storage:
    """ Класс описывающий склад """

    def __init__(self, stored_equipment):
        self.stored_equipment = stored_equipment

    def __str__(self):
        # Попытка отформатировать вывод. Почему-то такая конструкция не сработала:
        # json.loads(json.dumps(json_stored_equipment, indent=4, sort_keys=True)))
        formatted_string = self.stored_equipment.replace(" [", " \n  [")
        formatted_string = formatted_string.replace("], ", "], \n ")
        formatted_string = formatted_string.replace("}, ", "}, \n    ")
        formatted_string = formatted_string.replace("}]}", "}]\n}")
        return f'Данные склада: \n{json.loads(json.dumps(formatted_string))}'


# тестирование состояния склада
storage1 = Storage(str({
    "Принтеры":
        [
            {"equipment_id": "001", "name": "Epson-12345", "price": 12345, "printer_type": "Струйный"},
            {"equipment_id": "004", "name": "Epson-512", "price": 5432, "printer_type": "Лазерный"},
            {"equipment_id": "006", "name": "Epson-5111А", "price": 132, "printer_type": "Матричный"}
        ],
    "Сканеры":
        [
            {"equipment_id": "002", "name": "Epson-5432", "price": 5432, "printer_type": "Планшетный"}
        ]
}))

print(storage1)

# Далее см. "task_05.py"
