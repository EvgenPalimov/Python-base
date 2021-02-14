"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def get_material_size(self):
        pass


class Coat:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def coat(self):
        self.width = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на плащ, равняется: {self.width}.'


class Suit:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def suit(self):
        self.height = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм, равняется: {self.height}.'


class Textile(Coat, Suit):
    def __init__(self, width, height):
        super().__init__(width, height)

    @property
    def fabric_consumption(self):
        return str(f'Общий расход ткани, равняется: {round(self.width + self.height)}')


coat = Coat(5, 8)
suit = Suit(5, 8)
textile = Textile(5, 8)

print(coat.__str__())
print(suit.__str__())
print(textile.fabric_consumption)
