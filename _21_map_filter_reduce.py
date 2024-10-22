"""MAP, FILTER Y REDUCE

Son funciones que reciben como argumentos funciones que operan sobre
colecciones iterables.

Sintaxis:
- map(function, iterable)
- filter(function, iterable)

"""
from functools import reduce
from itertools import product


def _01_map_example():
    some_numbers: list[int] = [1, 2, 3, 4, 5]
    squared: list[int] = list(map(lambda x: x ** 2, some_numbers))
    print(f'some_numbers: {some_numbers}, with squares: {squared}')


def _02_filter_example():
    some_numbers: list[int] = [1, 2, 3, 4, 5]
    even_numbers: list[int] = list(filter(lambda x: x % 2 == 0, some_numbers))
    print(f'some_numbers: {some_numbers}')
    print(f'even_numbers: {even_numbers}')


def _03_reduce_example():
    some_numbers: list[int] = [1, 2, 3, 4, 5]
    prod = reduce(lambda x, y: x * y, some_numbers)
    print(f'product: {prod}')


def main():
    _01_map_example()
    print()

    _02_filter_example()
    print()

    _03_reduce_example()
    print()


if __name__ == '__main__':
    main()
