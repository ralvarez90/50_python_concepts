"""FUNCIONES Y SCOPE (ALCANCE)

1. Funciones
Son bloques de código reutilizable que efectúa una tarea concreta. Pueden o no
recibir parámetros y pueden o no regresar un valor.

La forma más común de definir funciones es empleando la palabra reservada def, de
la siguiente manera:

def nombre_funcion(p1, p2, ..., pn):
    ...
    ...
    return <Valor>

2. Scope (Alcance)
Cada función tiene su propio alcance, es decir los objetos definidos dentro de
estas solo existirán dentro del cuerpo de dicha función.

En otras palabras, es scope hace referencia a la visibilidad y alcance de variables
en distintas partes del código.

2.1 Scope Global
Son objetos definidos fuera de cualquier función o clase. Son accesibles desde cualquier
parte del código.

2.2 Scope local
Son variables definidas dentro de una función.

Nota:
- En python todas las funciones regresan un valor. Si no se especifica una instrucción
de retorno, implícitamente se retorna un None.
- Las funciones son fcc por lo que son tratados como cualquier otra variable.
"""

general_msg: str = 'Este es un string con scope global'


def _01_funciones():
    # función interna
    def say_hi():
        print(f'Hi from function say_hi inside of _01_funciones function')

    # invocamos
    say_hi()


def _02_funciones_con_retorno():
    return f'Este string es regresado por una función.'


def _03_alcance():
    some_str: str = 'Este string solo existe dentro de la función _03_alcance'
    print(some_str)
    print(f'general_msg: {general_msg}')


def main():
    _01_funciones()
    print()

    print(_02_funciones_con_retorno())
    print()

    _03_alcance()
    print()


if __name__ == '__main__':
    main()
