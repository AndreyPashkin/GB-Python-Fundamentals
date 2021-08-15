# 5. Продолжить работу над предыдущим[*] заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
# * - слово "первым" тут не подходит


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
        return f'Название принтера: {self.name}; \nЦена: {self.price} руб.; \nТип принтера: {self.printer_type}\n'


class Scanner(Equipment):
    def __init__(self, equipment_id, name, price, scanner_type):
        super().__init__(equipment_id, name, price)
        self.scanner_type = scanner_type

    def __str__(self):
        return f'Название сканера: {self.name}; \nЦена: {self.price}; \nТип сканера: {self.scanner_type}\n'


class Xerox(Equipment):
    def __init__(self, equipment_id, name, price, xerox_type):
        super().__init__(equipment_id, name, price)
        self.xerox_type = xerox_type

    def __str__(self):
        return f'Название копира: {self.name}; \nЦена: {self.price}; \nТип копира: {self.xerox_type}\n'


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
        for j, section in enumerate(stored_equipment):
            for i, item in enumerate(stored_equipment[section]):
                item["equipment_place"] = "Склад"
        self.stored_equipment = stored_equipment

    def __str__(self):
        result = ''
        for j, section in enumerate(self.stored_equipment):
            result += "-" * 65 + '\n'
            result += f'Тип оборудования: {section} \n'
            result += "{:>4} {:>15} {:>7} {:>15} {:>20} \n".format("ID", "Название", "Цена", "Тип", "Месторасположение")
            equipment_type = ""
            for i, item in enumerate(self.stored_equipment[section]):
                if section == 'Принтеры':
                    equipment_type = "printer_type"
                elif section == 'Сканеры':
                    equipment_type = "scanner_type"
                elif section == 'Ксероксы':
                    equipment_type = "xerox_type"
                result += "{:>4} {:>15} {:>7} {:>15} {:>20} \n".format(item["equipment_id"],
                                                                       item["name"],
                                                                       item["price"],
                                                                       item[equipment_type],
                                                                       item["equipment_place"])
        result += "-" * 65 + '\n'
        return f'Данные склада: \n{result}'

    def find_section(self, new_section):
        """ Проверка, есть ли уже такой раздел """
        result = False
        for j, section in enumerate(self.stored_equipment):
            if new_section == section:
                result = True
        return result

    def add_equipment(self, section, equipment):
        """ Добавление оборудования для учёта """
        equipment["equipment_place"] = "Склад"
        if self.find_section(section):
            # Если такой раздел уже есть - берём его, расширяем и заменяем в начальном словаре
            temp = self.stored_equipment[section]
            temp.append(equipment)
            self.stored_equipment[section] = temp
        else:
            # Если такого раздела ещё нет - добавляем
            self.stored_equipment[section] = [equipment]

    def move_equipment(self, equipment_id, place: str):
        """ Перемещение оборудования """
        for j, section in enumerate(self.stored_equipment):
            for i, item in enumerate(self.stored_equipment[section]):
                if equipment_id == item["equipment_id"]:
                    item["equipment_place"] = place

    def get_section_amount(self, section):
        return len(self.stored_equipment[section])


# тестирование состояния склада
storage1 = Storage({
    "Принтеры":
        [
            {"equipment_id": "001", "name": "Epson-12345", "price": 12345, "printer_type": "Струйный"},
            {"equipment_id": "004", "name": "Epson-512", "price": 5432, "printer_type": "Лазерный"},
            {"equipment_id": "006", "name": "Epson-5111А", "price": 132, "printer_type": "Матричный"}
        ],
    "Сканеры":
        [
            {"equipment_id": "002", "name": "Epson-5432", "price": 5432, "scanner_type": "Планшетный"}
        ]
})

# Тестирование добавления оборудования
printer5 = {"equipment_id": "008", "name": "Epson-501А", "price": 1322, "printer_type": "Матричный"}
storage1.add_equipment("Принтеры", printer5)

scanner2 = {"equipment_id": "028", "name": "HP-52JUY", "price": 1222, "scanner_type": "Ручной"}
storage1.add_equipment("Сканеры", scanner2)

copier1 = {"equipment_id": "018", "name": "Xerox-01w3А", "price": 13322, "xerox_type": "Тип 12"}
storage1.add_equipment("Ксероксы", copier1)

# Смотрим состояние учёта после добавления оборудования
print(storage1)

# Переносим один из принтеров в бухгалтерию
print('Переносим один из принтеров в бухгалтерию.')
storage1.move_equipment("004", "Бухгалтерия")
# Смотрим состояние учёта после переноса оборудования
print(storage1)

print(f'Количество принтеров: {storage1.get_section_amount("Принтеры")}')
print(f'Количество сканеров: {storage1.get_section_amount("Сканеры")}')
print(f'Количество ксероксов: {storage1.get_section_amount("Ксероксы")}')

# Далее см. "task_06.py"
