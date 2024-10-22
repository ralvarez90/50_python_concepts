"""FUNCIONES LAMBDA

Son conocidas como funciones anónimas, es decir funciones sin nombre que se pueden
usar como objetos de retorno o como argumentos de funciones.

Se definen empleando la palabra reservada lambda, posteriormente una list de parámetros
separados por comas y al final la expresión a evaluar.

Una función lambda solo puede contener una expresión corta.
"""
from typing import Callable

from numpy.random import randint


def _01_lambda_function():
    obtener_suma: Callable[[int, int], int] = lambda x, y: x + y
    print(f'obtener_suma(1, 2) -> {obtener_suma(1, 2)}')


def _02_lambda_functions_as_argument():
    number_points: int = 3
    points: list[tuple[int, int]] = [(randint(0, 100), randint(0, 100)) for _ in range(number_points)]
    print(f'original array points: {points}')
    points = sorted(points, key=lambda point: point[1])
    print(f'ordered  array points: {points}')


def _03_lambda_function():
    is_even: Callable[[int], bool] = lambda n: n % 2 == 0
    some_integer: int = randint(1, 100)
    print(f'some_integer: {some_integer}')
    print('Is even' if is_even(some_integer) else 'Is odd')


def main():
    _01_lambda_function()
    print()

    _02_lambda_functions_as_argument()
    print()

    _03_lambda_function()
    print()


if __name__ == '__main__':
    main()
