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


class Store:
    def __init__(self, initial_store=None):
        self.store = initial_store if initial_store is not None else {}

    def append(self, item, quantity):
        assert isinstance(quantity, int)
        assert quantity > 0
        if item not in self.store:
            self.store[item] = {"store": quantity}
        else:
            if "store" in self.store[item]:
                self.store[item]["store"] += quantity
            else:
                self.store[item]["store"] = quantity

    def move(self, item, departament, quantity):
        assert isinstance(quantity, int)
        assert quantity > 0
        if item not in self.store:
            raise ValueError("Нет такого оборудования на складе!")
        if self.store[item].get('store', 0) < quantity:
            raise ValueError("На складе нет нужного количества оборудования!")
        self.store[item]["store"] -= quantity
        if departament in self.store[item]:
            self.store[item][departament] += quantity
        else:
            self.store[item][departament] = quantity


class OfficeEquipment:
    def __init__(self, model, cost):
        self.cost = cost
        self.model = model

    def __repr__(self):
        return self.model


class Printer(OfficeEquipment):
    def __init__(self, model, cost, max_print_size):
        super().__init__(model, cost)
        self.max_print_size = max_print_size


class Scanner(OfficeEquipment):
    def __init__(self, model, cost, media_type):
        super().__init__(model, cost)
        self.media_type = media_type


class Copier(OfficeEquipment):
    def __init__(self, model, cost, color):
        super().__init__(model, cost)
        self.color = color


store = Store()
item = Printer("hp1320", 5000, "A4")

store.append(item, 10)
print(store.store)

store.move(item, "Продажи", 3)
print(store.store)

try:
    store.move(item, "Производство", 9)
    print(store.store)
except Exception as e:
    print(e)

store.move(item, "Производство", 6)
print(store.store)