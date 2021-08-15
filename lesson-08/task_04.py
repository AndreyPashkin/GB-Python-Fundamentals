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

    def __str__(self):
        return f'Название принтера: {self.name}; \nЦена: {self.price} руб.; \nТип принтера {self.printer_type}\n'


class Scanner(Equipment):
    def __init__(self, name, price, scanner_type):
        super().__init__(name, price)
        self.scanner_type = scanner_type

    def __str__(self):
        return f'Название сканера: {self.name}; \nЦена: {self.price}; \nТип сканера {self.scanner_type}\n'


class Xerox(Equipment):
    def __init__(self, name, price, xerox_type):
        super().__init__(name, price)
        self.xerox_type = xerox_type

    def __str__(self):
        return f'Название копира: {self.name}; \nЦена: {self.price}; \nТип копира {self.xerox_type}\n'


p1 = Printer("Epson-12345", 12345, "Струйный")
print(p1)

s1 = Scanner("Epson-5432", 5432, "Планшетный")
print(s1)

x1 = Xerox("Xerox-21345", 21345, "Цифровой")
print(x1)

# Далее см. "task_05.py"
