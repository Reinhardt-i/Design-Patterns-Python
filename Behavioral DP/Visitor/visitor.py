from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """The abstract base class for shapes."""

    @abstractmethod
    def accept(self, visitor: 'Visitor') -> None:
        """Accept a visitor."""
        pass


class Visitor(ABC):
    """The abstract base class for visitors."""

    @abstractmethod
    def visit(self, shape: Shape) -> None:
        """Visit a shape."""
        pass


class AreaVisitor(Visitor):
    """A concrete visitor to calculate the area of shapes."""

    def visit(self, shape: Shape) -> None:
        """Visit a shape and calculate its area."""
        if isinstance(shape, Circle):
            area = pi * shape.radius ** 2
            print(f"Area of Circle: {area}")
        elif isinstance(shape, Rectangle):
            area = shape.width * shape.height
            print(f"Area of Rectangle: {area}")
        elif isinstance(shape, Triangle):
            area = 0.5 * shape.base * shape.height
            print(f"Area of Triangle: {area}")


class Circle(Shape):
    """A concrete shape representing a circle."""

    def __init__(self, radius: float):
        self.radius = radius

    def accept(self, visitor: Visitor) -> None:
        """Accept a visitor and visit the circle."""
        visitor.visit(self)


class Rectangle(Shape):
    """A concrete shape representing a rectangle."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def accept(self, visitor: Visitor) -> None:
        """Accept a visitor and visit the rectangle."""
        visitor.visit(self)


class Triangle(Shape):
    """A concrete shape representing a triangle."""

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def accept(self, visitor: Visitor) -> None:
        """Accept a visitor and visit the triangle."""
        visitor.visit(self)


# Client code
if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 7)

    area_visitor = AreaVisitor()

    circle.accept(area_visitor)
    rectangle.accept(area_visitor)
    triangle.accept(area_visitor)

    # Output:
    # Area of Circle: 78.53981633974483
    # Area of Rectangle: 24
    # Area of Triangle: 10.5
    
    
    
def print_visitor_pattern_description():
        description = """
    The Visitor pattern allows you to define new operations on a collection of objects without modifying their classes. 
    It separates the algorithms (visitors) from the objects on which they operate (elements) by defining a common interface. 
    Elements accept visitors and delegate the appropriate operation to the visitor based on their type. This pattern is useful 
    when you want to add new behaviors to a set of objects without modifying their structure.

    In the code above, we have the Shape hierarchy consisting of the Circle, Rectangle, and Triangle classes. 
    We also have the Visitor hierarchy consisting of the abstract Visitor class and the concrete AreaVisitor class. 
    The Shape classes implement the accept method from the Shape interface, which allows them to accept a visitor and 
    call the visitor's visit method based on their type. The AreaVisitor class implements the visit method to calculate 
    and print the area of each shape.

    By using the Visitor pattern, we can easily add new operations (visitors) to the Shape hierarchy without modifying 
    the shape classes themselves. This promotes extensibility and separation of concerns, as each visitor encapsulates 
    a specific behavior that can be applied to multiple shape classes.
    """
    print(description.strip())
    