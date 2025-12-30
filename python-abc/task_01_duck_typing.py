<<<<<<< HEAD
#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> None:
        ...

    def perimeter(self) -> None:
        ...

class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())




=======
#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> None:
        ...

    def perimeter(self) -> None:
        ...

class Circle(Shape):
    def __init__(self, radius):
        if self.radius > 0:
            self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

>>>>>>> b1852ed (gitpusher)
