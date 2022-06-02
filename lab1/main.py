from lab1.model.Figures2D.Circle import Circle
from lab1.model.GeometryPrimitives.LineSegment import LineSegment
from lab1.model.Figures3D.Parallelepiped import Parallelepiped
from lab1.model.GeometryPrimitives.Point import Point
from lab1.model.Figures2D.Rectangle import Rectangle
from lab1.model.Figures3D.Sphere import Sphere


def main():
    p1 = Point(0, 0, 0)
    p2 = Point(3, 4, 0)
    segment = LineSegment(p1, p2)
    print("Segment's length: ", segment.length)

    c = Circle(2)
    print("Circle's area: ", c.area)

    r = Rectangle(4, 2)
    print("Rectangle's area: ", r.area)

    sphr = Sphere(1)
    print("Sphere's volume:", sphr.volume)
    print("Sphere's surface area:", sphr.surface_area)

    parlpided = Parallelepiped(3, 4, 5)
    print("Parallelepiped's volume:", parlpided.volume)
    print("Parallelepiped's surface area:", parlpided.surface_area)


if __name__ == '__main__':
    main()
