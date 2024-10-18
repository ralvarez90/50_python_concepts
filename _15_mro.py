"""METHOD RESOLUTION ORDER

Este determina el orden en el que las clases busca los atributos y métodos dentro de una
jerarquía de herencia. Esto debido a que python soporta herencia múltiple.

El __mro__ es crucial para determinar qué implementaciónes invocar. Python usa el algoritmo
C3 de linearización para proporcionar un mecanismo robusto y consistente para determinar
el orden de resolución de métodos.
"""


class A:
    def some_method(self):
        print('Método en A')


class B:
    def some_method(self):
        print('Método en B')


class C(A, B):
    def some_method(self):
        print(f'Método en C')


def _01_mro_example():
    c = C()
    c.some_method()
    print(C.__mro__)


def main():
    _01_mro_example()
    print()


if __name__ == '__main__':
    main()
