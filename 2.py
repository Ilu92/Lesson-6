# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.

class Road:
    def __init__(rut, _length, _width):
        rut._length = _length
        rut._width = _width

    def mass(rut):
        return rut._length * rut._width


class MassCount(Road):
    def __init__(rut, _length, _width, volume):
        super().__init__(_length, _width)
        rut.volume = volume


r = MassCount(25, 10000, 125)
print(r.mass())