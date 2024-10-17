"""STRINGS

Son cadenas inmutables de caracteres bajo la clase str. Son secuencias iterables e
indexable con la posibilidad de usar la técnica de slicing como las listas.

Podemos concatenarlos usando el operador + o el méthod concat. Existen divesos
mecanismos para mostrar strings con formato.
"""


def _01_creating_strings():
    full_name: str = 'Rodrigo Álvarez'
    print(f'full_name: {full_name}, with length: {len(full_name)}')
    for i, _ in enumerate(full_name):
        print(f'full_name[{i}]: {full_name[i]}')


def _02_slicing():
    full_name: str = 'John Wick'
    tail_sice: int = len(full_name)
    for _ in full_name:
        print(f'full_name[0:{tail_sice}]: {full_name[0:tail_sice]}')
        tail_sice -= 1


def main():
    _01_creating_strings()
    print()

    _02_slicing()
    print()


if __name__ == '__main__':
    main()
