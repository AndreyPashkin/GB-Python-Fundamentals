# 6. Продолжить работу над предыдущим[*] заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
# * - слово "вторым" тут не подходит

class Error(Exception):
    """Базовый класс для ошибок"""
    pass


class WrongIdValue(Error):
    """Некорректное значение для идентификатора"""
    pass


class WrongPriceValue(Error):
    """Некорректное значение для цены"""
    pass


class WrongNameValue(Error):
    """Некорректное значение для названия"""
    pass


class WrongTypeValue(Error):
    """Некорректное значение для марки оборудования"""
    pass


class WrongSectionName(Error):
    """Некорректное значение для вида оборудования"""
    pass


class Equipment:
    def __init__(self, equipment_id, name, price):
        try:
            self.equipment_id = equipment_id
            self.name = name
            self.price = price

            if not equipment_id:
                raise WrongIdValue(f'Ошибка! Не указано значение для идентификатора.')
            if not name:
                raise WrongNameValue(f'Ошибка! Не указано значение для названия.')
            if not price:
                raise WrongNameValue(f'Ошибка! Не указано значение для цены')
            elif (type(price) is not int) and (type(price) is not float):
                raise WrongNameValue(f'Ошибка! Указано значение для цены не числового типа: {price}')

        except WrongIdValue as error:
            print(error)

        except WrongNameValue as error:
            print(error)

        except WrongPriceValue as error:
            print(error)


class Printer(Equipment):
    def __init__(self, equipment_id, name, price, printer_type):
        super().__init__(equipment_id, name, price)
        try:
            self.printer_type = printer_type
            if not printer_type:
                raise WrongTypeValue(f'Ошибка! Не указано значение для марки принтера.')
        except WrongTypeValue as error:
            print(error)

    def __str__(self):
        return f'Название принтера: {self.name}; \nЦена: {self.price} руб.; \nТип принтера: {self.printer_type}\n'


class Scanner(Equipment):
    def __init__(self, equipment_id, name, price, scanner_type):
        super().__init__(equipment_id, name, price)
        try:
            self.scanner_type = scanner_type
            if not scanner_type:
                raise WrongTypeValue(f'Ошибка! Не указано значение для марки сканера.')
        except WrongTypeValue as error:
            print(error)

    def __str__(self):
        return f'Название сканера: {self.name}; \nЦена: {self.price}; \nТип сканера: {self.scanner_type}\n'


class Xerox(Equipment):
    def __init__(self, equipment_id, name, price, xerox_type):
        super().__init__(equipment_id, name, price)
        try:
            self.xerox_type = xerox_type
            if not xerox_type:
                raise WrongTypeValue(f'Ошибка! Не указано значение для марки копира.')
        except WrongTypeValue as error:
            print(error)

    def __str__(self):
        return f'Название копира: {self.name}; \nЦена: {self.price}; \nТип копира: {self.xerox_type}\n'


# тестирование создания записей об оборудовании
p1 = Printer("001", "Epson-12345", 12345, "Струйный")
print(p1)

s1 = Scanner("002", "Epson-5432", 5432, "Планшетный")
print(s1)

x1 = Xerox("003", "Xerox-21345", 21345, "Цифровой")
print(x1)

print("========= С ошибками =========")
x2 = Xerox("", "Xerox-21345", 21345, "Цифровой")
x3 = Xerox("013", "", 21345, "Цифровой")
x4 = Xerox("014", "Xerox-21345", "", "Цифровой")
x5 = Xerox("015", "Xerox-21345", "цена", "Цифровой")
x6 = Xerox("016", "Xerox-21345", "23456", "Цифровой")
p30 = Printer("030", "HP-20001", 1234, "")
s31 = Scanner("031", "HP-201", 2345, "")
x32 = Xerox("032", "Xerox-201", 3456, "")
print("\n")


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

    def check_section(self, new_section):
        """ Проверка, есть ли уже такой раздел """
        result = False
        for j, section in enumerate(self.stored_equipment):
            if new_section == section:
                result = True
        return result

    def check_item(self, equipment_id):
        """ Проверка, есть ли уже оборудование с таким ID """
        exists = False
        for j, section in enumerate(self.stored_equipment):
            for i, item in enumerate(self.stored_equipment[section]):
                if equipment_id == item["equipment_id"]:
                    exists = True
        return exists

    def add_equipment(self, section, equipment):
        """ Добавление оборудования для учёта """
        equipment["equipment_place"] = "Склад"
        if self.check_section(section):
            # Если такой раздел уже есть - берём его, расширяем и заменяем в начальном словаре
            temp = self.stored_equipment[section]
            temp.append(equipment)
            self.stored_equipment[section] = temp
        else:
            # Если такого раздела ещё нет - добавляем
            self.stored_equipment[section] = [equipment]

    def move_equipment(self, equipment_id, place: str):
        """ Перемещение оборудования """
        try:
            if not self.check_item(equipment_id):
                raise WrongIdValue(f'Оборудования с идентификатором {equipment_id} на учёте нет.')
            for j, section in enumerate(self.stored_equipment):
                for i, item in enumerate(self.stored_equipment[section]):
                    if equipment_id == item["equipment_id"]:
                        item["equipment_place"] = place
        except WrongIdValue as error:
            print(error)

    def get_section_amount(self, section):
        try:
            if (section != "Принтеры") and (section != "Сканеры") and (section != "Ксероксы"):
                raise WrongSectionName(f'Ошибка! Оборудование такого вида склад не принимает.')
            return len(self.stored_equipment[section])

        except WrongSectionName as error:
            print(error)


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
storage1.move_equipment("999", "Монтажный отдел")  # Ошибка

# Смотрим состояние учёта после переноса оборудования
print(storage1)

print(f'Количество принтеров: {storage1.get_section_amount("Принтеры")}')
print(f'Количество сканеров: {storage1.get_section_amount("Сканеры")}')
print(f'Количество ксероксов: {storage1.get_section_amount("Ксероксы")}')
print(f'Количество пылесосов: {storage1.get_section_amount("Пылесосов")}')  # Ошибка
