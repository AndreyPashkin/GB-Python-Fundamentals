# 5. Продолжить работу над предыдущим[*] заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
# * - слово "первым" тут не подходит

# Ещё доделываю. Выложил, чтобы вписаться во время. Пока сделаны задания 1, 2, 3, 4, 7


class Equipment:
    def __init__(self, name: str, price: float, location: str):
        self.name = name
        self.price = price
        self.location = location

    def take_to_storage(self, info_storage: dict):
        self.location = "Склад"

    def move_to_subdivision(self, subdivision: str, info_storage: dict):
        self.location = subdivision


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

# Ещё доделываю. Выложил, чтобы вписаться во время. Пока сделаны задания 1, 2, 3, 4, 7
