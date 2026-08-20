from abc import ABC, abstractmethod
import math


# --------------------------------
# Abstract Shape
# --------------------------------

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# --------------------------------
# Vector Class
# --------------------------------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Vector addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Vector equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Compare vector magnitudes
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


# --------------------------------
# Circle Class
# --------------------------------

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    # Compare circles by radius
    def __lt__(self, other):
        return self.radius < other.radius

    # Compare circles
    def __eq__(self, other):
        return self.radius == other.radius

    # String representation
    def __str__(self):
        return f"Circle(radius={self.radius})"


# --------------------------------
# Example
# --------------------------------

v1 = Vector(3, 4)
v2 = Vector(2, 1)

v3 = v1 + v2

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Vector addition:", v3)

print("Vector magnitude:", v1.magnitude())
print("v1 == v2:", v1 == v2)
print("v1 < v2:", v1 < v2)


circle1 = Circle(5)
circle2 = Circle(7)

print("\nCircle 1:", circle1)
print("Area:", circle1.area())
print("Perimeter:", circle1.perimeter())

print("\nCircle 1 == Circle 2:", circle1 == circle2)
print("Circle 1 < Circle 2:", circle1 < circle2)
