from lab1.model.Figures3D.Figure3D import Figure3D


class Parallelepiped(Figure3D):
    def __init__(self, width: int, length: int, height: int):
        self.__width = width
        self.__length = length
        self.__height = height

    @property
    def volume(self) -> float:
        return self.__height * self.__width * self.__length

    @property
    def surface_area(self) -> float:
        return 4 * self.__width * self.__length + 2 * self.__width * self.__height
