"""CLASES Y OBJETOS

1. Clases
Son planos o plantillas para crear objetos. En estas se define el comportamiento y
los atributos de los objetos creados a partir de dichas clases

2. Objetos
Son instancias de clases.

Usamos __init__ para inicializar el estado de los objetos. Este se invoca justo después
de invocar __new__.
"""


class MyClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def my_method(self):
        return self.x + self.y


def _01_classes_and_objects():
    some_instance: MyClass = MyClass(1, 2)
    result = some_instance.my_method()
    print(f'some_instance.my_method result: {result}')


def main():
    _01_classes_and_objects()


if __name__ == '__main__':
    main()
