"""DICCIONARIOS

Son colecciones no ordenadas de pares clave-valor. Son mutables y son instancias de
la clase dict.

Accedemos a cade valor de un par por medio de su key. Podemos obtener iterables
de las llaves y valores usando los métodos keys y values respectivamente.

Los diccionarios son usados frecuentemente para representar datos estructurados, como
perfiles de usuario, configuraciones, registros de bases de datos, etc.

También se usan como mecanismo para pasar argumentos nombrados a funciones y
métodos. Son de las estructuras de datos más importantes.   
"""


def _01_define_dictionary():
    some_dict: dict = {
        'name': 'Peter',
        'age': 23,
        'is_single': False,
    }
    print(f'some_dict: {some_dict}, with length: {len(some_dict)}')


def _02_keys_values_items_methods():
    numbers_dict: dict = {'one': 1, 'two': 2, 'three': 3}
    print(f'numbers_dict: {numbers_dict}')
    print(f'Call keys method  : {[key for key in numbers_dict.keys()]}')
    print(f'Call values method: {[value for value in numbers_dict.values()]}')
    print(f'Call items method : {[(k, v) for k, v in numbers_dict.items()]}')


def main():
    _01_define_dictionary()
    print()

    _02_keys_values_items_methods()
    print()


if __name__ == '__main__':
    main()
