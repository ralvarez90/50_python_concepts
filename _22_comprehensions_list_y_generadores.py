"""COMPREHENSIONS LIST Y GENERADORES

1. Comprehensions List
Básicamente consiste en construir listas usando con base en otras listas
o iterables, expresiones y condiciones.

2. Generadores
Son similares a las listas por comprensión, con la diferencia de que estos
van entregando sus valores correspondientes bajo demanda, por ese se dice
que son de evaluación perezosa.

En su interior un generador emplea la palabra reservada yield para devolver
cada valor de una secuencia.

Los generadores son más eficientes en memoria
"""
from typing import Generator


def _01_comprehension_list():
    lower_bound: int = int(input('Integer lower_bound: '))
    upper_bound: int = int(input('Integer upper_bound: '))
    some_squares: list[int] = [x ** 2 for x in range(lower_bound, upper_bound)]
    print(f'some_squares: {some_squares}')


def _02_comprehension_list():
    even_numbers: list[int] = [x for x in range(1, 11) if x % 2 == 0]
    print(f'even_numbers: {even_numbers}')


def _03_generadores():
    # generador propio
    def rango(n: int):
        for _item in range(n):
            yield _item

    generador_primeros_10 = rango(10)
    for i in generador_primeros_10:
        print(i, end=' ')
    print()


def _04_generadores():
    generador_primeros_10 = (i for i in range(10))
    for i in generador_primeros_10:
        print(i, end=' ')
    print()


def _05_generadores():
    even_numbers_generator: Generator[int, None, None] = (x for x in range(1, 11) if x % 2 == 0)
    for n in even_numbers_generator:
        print(n, end=' ')
    print()


def main():
    _01_comprehension_list()
    print()

    _02_comprehension_list()
    print()

    _03_generadores()
    print()

    _04_generadores()
    print()


if __name__ == '__main__':
    main()
