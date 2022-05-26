class Point:
    def __init__(self, x: int, y: int, z: int):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def z(self) -> int:
        return self.__z
