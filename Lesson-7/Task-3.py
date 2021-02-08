"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
(не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
"""


class Microbe:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Microbe(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Microbe(self.quantity - other.quantity)
        else:
            print(f"{self.quantity} - {other.quantity}: Не возможная операция.")

    def __mul__(self, other):
        return Microbe(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Microbe(round(self.quantity // other.quantity))

    def __floordiv__(self, other):
        return Microbe(round(self.quantity // other.quantity))

    def make_order(self, per_row: int) -> str:
        rows, tail = self.quantity // per_row, self.quantity % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self.quantity} ячеек"


c1 = Microbe(17)
print(c1)
c2 = Microbe(13)
print(c2)

print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c2 * c2)
print(c1 // c2)
print(c1 / c2)
print((c1 * c2).make_order(23))
