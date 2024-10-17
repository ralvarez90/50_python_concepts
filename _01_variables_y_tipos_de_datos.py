"""VARIABLES Y TIPOS DE DATOS

1. Variables
Son nombres identificadores de espacios de memoria en donde almacenamos datos. Las variables en
python tienen un tipo de datos que se asigna de manera dinámica conforme al dato que almacena.

2. Tipos de datos
En python existen tipos de datos que se pueden utilizar sin necesidad de importar clases. Estos
tipos 'básicos' son: int, float, int, bool, str, list, tuple, dict, set, etc.

Notas:
- Python es un lenguaje orientado a objetos y basado en clases.
- Todas las variables en python son objetos.
- Para obtener el tipo de dato de un objeto empleamos la clase 'función' type
"""


def _01_variables():
    # integer value
    x: int = 123
    print(f'x has a value {x} and type "{type(x)}")')

    # string instance
    my_name: str = 'John Wick'
    print(f'Hello, my name is {my_name}')

    # list object
    some_integers: list[int] = [1, 2, 3, 4, 5]
    print(f'some_integers: {some_integers}, with type: "{type(some_integers)}"')


def main():
    _01_variables()
    print()

    if __name__ == '__main__':
        main()
