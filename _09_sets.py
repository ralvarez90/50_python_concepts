"""SETS

Colecciones no ordenadas de elementos únicos. Son instancias de la clase
set y obedecen a las reglas y lógicas de los conjuntos matemáticos.

Son colecciones no indexadas por lo que no podemos acceder a sus elementos
por medio de índices. Podemos usar el operador de contención in.
"""
from random import randint


def _01_creating_set():
    some_set: set[int] = {1, 2, 3}
    some_set.add(5)
    print(f'some_set: {some_set}, with length: {len(some_set)}, and type: {type(some_set)}')


def _02_membership_test():
    random_numbers_set: set[int] = set([randint(1, 100) for _ in range(10)])
    print(f'random_numbers_set: {random_numbers_set}')
    print(f'34 is in random_numbers_set: {34 in random_numbers_set}')


def main():
    _01_creating_set()
    print()

    _02_membership_test()
    print()


if __name__ == '__main__':
    main()
