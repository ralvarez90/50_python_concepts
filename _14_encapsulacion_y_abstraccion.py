"""ENCAPSULACIÓN Y ABSTRACCIÓN

Son principios de la programación orientada a objetos que contribuyen a construir software
modular, mantenible y escalable.

1. Encapsulación
Consiste en el aislamiento de las propiedades y métodos de los objetos de manera que
su funcionamiento interno permanezca oculto y aislado del exterior.

2. Abstracción
La abstracción es el proceso de simplificación de sistemas complejos por medio de la
representación de solo sus características esenciales.

Notas:
- Se considera buena práctica extender nuestras clases a partir de interfaces bien
definidas. Empleamos el paquete abs para manejar elementos abstractos como clases
y métodos.
"""
from abc import ABC, abstractmethod


class Car:
    """Using this class as encapsulation example."""

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def drive(self):
        return f'Driving {self.make} {self.model}'


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


def _01_using_classes():
    r1: Rectangle = Rectangle(1, 2)
    print(r1)
    print(f'Area     : {r1.area()}')
    print(f'Perimeter: {r1.perimeter()}')


def main():
    _01_using_classes()


if __name__ == '__main__':
    main()
