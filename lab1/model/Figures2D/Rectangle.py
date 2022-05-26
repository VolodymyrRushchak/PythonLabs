from lab1.model.Figures2D.Figure2D import Figure2D


class Rectangle(Figure2D):
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    @property
    def area(self) -> float:
        return self.__width * self.__height
