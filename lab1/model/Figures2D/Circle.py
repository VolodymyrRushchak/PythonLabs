from lab1.model.Figures2D.Figure2D import Figure2D
from math import pi


class Circle(Figure2D):
    def __init__(self, radius: int):
        self.__radius = radius

    @property
    def area(self) -> float:
        return pi * self.__radius ** 2
