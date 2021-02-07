"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} начал движение.'

    def stop(self):
        return f'Автомобиль {self.name} оставновился.'

    def turn(self, direction):
        """ Задает поворот авто в движении
        :param direction: направление поворота ('left', 'right')
        """
        if direction == 'left':
            return f'Автомобиль {self.name} поварачивает налево.'
        elif direction == 'right':
            return f'Автомобиль {self.name} поварачивает направо.'
        elif direction not in ('left', 'right'):
            return 'Не верно, задано направление.'

    def show_speed(self):
        return f'Текуща скорость {self.name} равнется: {self.speed}км/ч.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текуща скорость {self.name} равнется: {self.speed} км/ч.')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} превышай максимальную скорость ' \
                   f'в городе 60 км/ч.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текуща скорость {self.name} равнется: {self.speed} км/ч.')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} превышай максимальную скорость ' \
                   f'учебной езды, скорость должна состовлять не более 40 км/ч.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - это полицейская машина.'
        else:
            return f'{self.name} - это не полицейская машина.'


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(70, 'White', 'Oka', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(lada.turn('right'))
print(f'{oka.turn("left")}, затем {audi.stop()}')
print(f'{lada.go()} {lada.show_speed()}')
print(f'Автомобиль {lada.name} - {lada.color} цвета.')
print(f'Автомобиль {audi.name} полицейская машина? {audi.is_police}')
print(f'Автомобиль {lada.name} полицейская машина? {lada.is_police}')
print(audi.show_speed())
print(ford.show_speed())
print(oka.show_speed())
