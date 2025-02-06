from abc import ABC, abstractmethod
import math

"""
This module defines an abstract class Shape and its concrete
subclasses Circle and Rectangle.
Each subclass implements methods to calculate area and perimeter.
A function shape_info is provided to print these values for any shape instance.
"""


# Abstract Shape class
class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Circle class inheriting from Shape
class Circle(Shape):
    """Class representing a circle with a given radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle class inheriting from Shape
class Rectangle(Shape):
    """Class representing a rectangle with a given width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Function using duck typing to get shape information
def shape_info(shape):
    """Prints the area and perimeter of a given shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Testing
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle:")
shape_info(circle)

print("\nRectangle:")
shape_info(rectangle)
