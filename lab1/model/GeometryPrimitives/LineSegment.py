from lab1.model.GeometryPrimitives.Point import Point
from math import sqrt


class LineSegment:
    def __init__(self, start_point: Point, end_point: Point):
        self.__start_point = start_point
        self.__end_point = end_point

    @property
    def length(self) -> float:
        return sqrt((self.__start_point.x - self.__end_point.x)**2 +
                    (self.__start_point.y - self.__end_point.y)**2 +
                    (self.__start_point.z - self.__end_point.z)**2)
