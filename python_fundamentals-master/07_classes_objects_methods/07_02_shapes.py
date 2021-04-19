'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
from math import pi
class Rectangle():

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area_rectangle(self):
        area = self.length * self.width
        return f"The area of this rectangle: {area} "

    def perimeter_rectangle(self):
        perimeter = 2 * (self.length + self.width)
        return f"The perimeter of this rectangle: {perimeter}"

class Circle():

    def __init__(self, radius) -> None:
        self.radius = radius

    def area_circle(self):
        area = pi * self.radius**2
        return f"The area of this circle: {area:.2f}"

    def circumference_circle(self):
        circumference = 2 * (pi * self.radius**2)
        return f"The circumference of this circle: {circumference:.2f}"

some_rect = Rectangle(5,10)
some_circ = Circle(7)

print(some_rect.area_rectangle())
print(some_circ.area_circle())
print(some_rect.perimeter_rectangle())
print(some_circ.circumference_circle())