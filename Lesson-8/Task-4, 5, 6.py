"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


# ----------------------------------- 5 ----------------------------------------

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.

# ----------------------------------- 6 ----------------------------------------

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""


class OfficeEquipment:
    def __init__(self, name: str, price: int, quantity: int, modele: str = None, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.modele = modele
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def reception(self):
        unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity,
                'Тип техники': self.modele}
        self.my_unit.update(unit)
        return f'Ваше устройство добавлено на склад -\n {unit}', self.my_unit

    def transfer(self):
        pass
    # Не знаю как реализоать данную функцию.


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__(modele='Принтер', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__(modele='Сканер', *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__(modele='Ксерокс', *args)


unit_1 = Printer('HP', 2000, 5)
unit_2 = Scanner('Canon', 1200, 5)
unit_3 = Xerox('Xerox', 1500, 1)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())


