"""TUPLAS

Son colecciones inmutables de elementos. Similares a las listas aunque suelen ser
de un mismo tipo de dato.

Es el mecanismo que permite el "retorno múltiple" en python. Son instancias de la
clase tuple.

También podemos acceder a cada uno de sus elementos por medio de índices. También
pueden iterarse con for, y obtener sub tuplas mediante slicing.

Se le dice packing y unpacking al proceso de empacar multiples valores en una sola
tupla y unpacking al extraer los elementos de una tupla de manera individual.
"""


def _01_tuple():
    some_tpl: tuple[int, int, int] = (1, 2, 3)
    print(f'some_tpl: {some_tpl}, with len: {len(some_tpl)}')


def _02_tuple_slicing():
    other_tuple: tuple[int, int, int, str, str, str] = (1, 2, 3, 'a', 'b', 'c')
    print(f'other_tuple: {other_tuple}, with len: {len(other_tuple)}')
    print(f'tail of other_tuple: {other_tuple[1::]}')


def _03_packing():
    other_tuple = 1, 2, 3
    print(f'other_tuple: {other_tuple}')


def _04_unpacking():
    first, *second = (1, 2, 3, 4, 5)
    print(f'After "first, *second = (1, 2, 3 4, 5)"')
    print(f'first: {first}, second: {second}')


def _05_multiple_return():
    def get_origin() -> tuple[int, int]:
        return 0, 0

    my_origin = get_origin()
    print(f'my_origin: {my_origin}')


def main():
    _01_tuple()
    print()

    _02_tuple_slicing()
    print()

    _03_packing()
    print()

    _04_unpacking()
    print()

    _05_multiple_return()
    print()


if __name__ == '__main__':
    main()
