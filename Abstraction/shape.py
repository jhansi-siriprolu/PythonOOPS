from abc import ABC, abstractmethod


### make ABC as parent class for parent class
### add tag @abstractmethod before defining abstract method
### You will not be able to create Circle object
### without creating area method in it as making @abstractmethod in parent
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius


class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width
