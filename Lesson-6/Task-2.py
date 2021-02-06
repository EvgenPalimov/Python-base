"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    # удельная масса 1кв.м. дорожного полотна толщиной 1 см (тонн)
    _weight_asphalt: float = 0.02

    def __init__(self, length: [int, float], width: [int, float]):
        self._length = float(length)
        self._width = float(width)

    # param thickness: Толщина дорожного покрытия в сантиметрах.
    # return: Масса дорожного полотна в тоннах если все ОК, иначе None
    def asphalt_coating(self, thickness: float) -> [float, None]:
        try:
            return self._length * self._width * thickness * self._weight_asphalt
        except TypeError:
            return None


road = Road(5000, 20)
print(f'Масса дорожного покрытия составит: {road.asphalt_coating(5)} тонн.')
