# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Equipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(Equipment):
    def __init__(self, name, price, printer_type):
        super().__init__(name, price)
        self.printer_type = printer_type


class Scanner(Equipment):
    def __init__(self, name, price, scanner_type):
        super().__init__(name, price)
        self.scanner_type = scanner_type


class Xerox(Equipment):
    def __init__(self, name, price, xerox_type):
        super().__init__(name, price)
        self.xerox_type = xerox_type

# Далее см. "task_05.py"
