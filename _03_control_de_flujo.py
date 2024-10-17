"""CONTROL DE FLUJO

Permiten modificar el flujo de un programa con base en condiciones. En primera
instancia tenemos los clásicos if, elif, else.

1. Uso de if, elif, else
Son básicamente el if, else if y else de lenguajes como java. Se usa
un booleano o expresión que se evalúe como booleano en el if, y elif. Se
emplea el else en caso de que no se cumple una condición del if o elif.

2. Loop for
Se emplea para iterar sobre cada elemento de una secuencia iterable. La sintaxis
es:
for item in sequence:
    ...
    ...

Donde cada item es un elemento de la secuencia.

3. Loop while
Se ejecuta el bloque de código asignado siempre que la condición a evaluar sea
verdadera.
"""


def _01_if_elif_else_example():
    x: int = 10
    print(f'x: {x}')
    if x > 10:
        print('x is greater than 10')
    elif x < 10:
        print('x is less than 10')
    else:
        print('x is equal to 10')


def _02_for_loop():
    fruits: list[str] = ['Apple', 'Banana', 'Orange']
    print(f'fruits: {fruits}')
    for fruit in fruits:
        print(f'- {fruit.title()}')


def _03_while_loop():
    i: int = 1
    while i <= 10:
        print(f'i -> {i}')
        i += 1


def main():
    _01_if_elif_else_example()
    print()

    _02_for_loop()
    print()

    _03_while_loop()
    print()


if __name__ == '__main__':
    main()
