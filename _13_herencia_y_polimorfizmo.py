"""HERENCIA Y POLIMORFISMO

La herencia y el polimorfismo son pilares dentro de la POO. En python no
existe la sobrecarga, se solventa usando default parameters.

La herencia y el polimorfismo son conceptos poderosos en la programación
orientada a objetos, ya que promueve la reutilización de código, modularidad
y flexibilidad.
"""


class Animal:
    def sound(self) -> str:
        return f'Some generic sound'


class Dog(Animal):
    def sound(self) -> str:
        return 'Woof'


class Cat(Animal):
    def sound(self) -> str:
        return 'Meow'


class Calculator:
    def add(self, a, b=0):
        return a + b


def _01_instances():
    some_dog: Dog = Dog()
    print(some_dog.sound())

    some_cat: Cat = Cat()
    print(some_cat.sound())


def _02_overloading_achieved():
    calc: Calculator = Calculator()
    print(calc.add(2, 3))
    print(calc.add(2))


def main():
    _01_instances()
    print()


if __name__ == '__main__':
    main()
