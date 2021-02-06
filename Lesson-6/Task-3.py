"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self, reverse=False):
        """
        Собирает полное имя для позиции в порядке 'заданном reverse
        :param reverse: порядок следования если False (по умолчанию) 'name surname'
        если True, то 'surname name'
        """
        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):
        return sum(self._income.values())


position_data = [
    {
        'name': 'Иван',
        'surname': 'Иванов',
        'position': 'Мастер',
        'wage': 40000,
        'bonus': 0
    },
    {
        'name': 'Сергей',
        'surname': 'Фралов',
        'position': 'Директор',
        'wage': 90000,
        'bonus': 60000
    },
    {
        'name': 'Ирина',
        'surname': 'Власова',
        'position': 'Зам. директора',
        'wage': 60000,
        'bonus': 30000
    },
]

for item in position_data:
    position = Position(**item)

    print('-' * 40)
    print('Имя: ', position.name)
    print('Фамилия: ', position.surname)
    print('Полное имя: ', position.get_full_name())
    print('Полное имя, на оборот: ', position.get_full_name(reverse=True))
    print('Должность: ', position.position)
    print(f'Полный доход сотрудника: {position.get_total_income()} руб.')
    print('-' * 40)
