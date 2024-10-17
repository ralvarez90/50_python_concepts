"""LISTAS

Son colecciones de objetos. Estas son indexadas e inmutables. Son instancias
de la clase list. Al ser instancias de list estas tiene sus propios métodos.

Podemos usar la función len para obtener su número de elementos, y el operador
in para verificar contención de elementos
"""
from random import randint


def _01_list_example():
    lst1: list = [1, 2, 3]
    lst2: list = [4, 5, 6]
    lst3: list = lst1 + lst2
    print(f'lst1: {lst1}')
    print(f'lst2: {lst2}')
    print(f'lst3: {lst3}')


def _02_len_example():
    empty_list: list = []
    print(f'empty_list: {empty_list}, with len: {len(empty_list)}')


def _03_in_operator_example():
    some_integers: list[int] = [randint(1, 100) for _ in range(10)]
    print(f'some_integers: {some_integers}, with len: {len(some_integers)}')
    print(f'5 in some_integers: {5 in some_integers}')


def main():
    _01_list_example()
    print()

    _02_len_example()
    print()

    _03_in_operator_example()
    print()


if __name__ == '__main__':
    main()
