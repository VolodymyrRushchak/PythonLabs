from lab1.model.Figures3D.Figure3D import Figure3D
from math import pi


class Sphere(Figure3D):
    def __init__(self, radius: int):
        self.__radius = radius

    @property
    def volume(self) -> float:
        return (4 / 3) * pi * self.__radius ** 3

    @property
    def surface_area(self) -> float:
        return 4 * pi * self.__radius ** 2
