"""OPERADORES Y EXPRESIONES

1. Operadores
Son símbolos que se emplean para realizar acciones entre objetos. Existen
de diversos tipos como:

1.1 Aritméticos
Son los clásicos de otros lenguajes de programación.

1.2 Relacionales (comparación)
Retorna un valor booleano resultado de compararlos. Son los clásicos
de siempre.

1.3 Lógicos
Son los mismos de otros lenguajes aunque en python se emplean con las
palabras reservadas and, or y not.

1.4 Asignación
Combinan los aritméticos y el de asignación. Básicamente simplifican realizar
una operación aritmética y luego asignar el resultado. Son los clásicos:
=, +=, -=, *=, /=, %=, **= y //=.

1.5 Bitwise
Conocidos como bit a bit, son operadores sobre enteros a nivel de bit. Es decir
son operadores lógicos que operan sobre enteros.

1.6 Identidad
Se emplea para comprar si dos objetos almacenan la misma referencia. Únicamente
tenemos is y la negación is not.

1.7 Pertenencia (membership)
Permiten saber si un valor se encuentra dentro de una secuencia. Es el in y la
negación not in.

2. Expresiones
Una expresión es un grupo de sentencias que se evalúan reduciéndose a un valor
concreto.

Notas:
- Podemos emplear la función bin para obtener la representación en base 2 de un
entero.
"""


def _01_arithmetics():
    a = 10
    b = 3
    print(f'Addition      : {a}  +  {b} = {a + b}')
    print(f'Subtraction   : {a}  -  {b} = {a - b}')
    print(f'Multiplication: {a}  *  {b} = {a * b}')
    print(f'Division      : {a}  /  {b} = {a / b}')
    print(f'Modulus       : {a}  %  {b} = {a % b}')
    print(f'Exponentiation: {a}  ^  {b} = {a ** b}')
    print(f'Floor Division: {a} //  {b} = {a // b}')


def _02_relational_comparison():
    x = 5
    y = 10
    print(f'{x} == {y}  ->  {x == y}')
    print(f'{x} != {y}  ->  {x != y}')
    print(f'{x} <  {y}  ->  {x < y}')
    print(f'{x} <= {y}  ->  {x <= y}')
    print(f'{x} >  {y}  ->  {x > y}')
    print(f'{x} >= {y}  ->  {x >= y}')


def _03_logical():
    v: bool = True
    f: bool = False
    print(f'{v} and {v} -> {v and v}')
    print(f'{v} or  {f} -> {v or f}')
    print(f'not {v} -> {not v}')
    print(f'not {f} -> {not f}')


def _04_assigment():
    x = 5
    print(f'x = {x}')
    x += 2
    print(f'After x += 2 -> x={x}')

    y = 10
    print(f'y = {y}')
    y -= 3
    print(f'After y -= 3 -> y={y}')


def _05_bitwise():
    a = 60
    b = 13
    bitwise_and = a & b
    bitwise_or = a | b
    bitwise_xor = a ^ b
    bitwise_not_a = ~a
    bitwise_left_shift = a << b
    bitwise_right_shift = a >> b

    print(f'a = {a}, in base 2: "{bin(a)}"')
    print(f'a = {b}, in base 2: "{bin(b)}"')
    print(f'a & b -> {bitwise_and} "{bin(bitwise_and)}"')
    print(f'a | b -> {bitwise_or} "{bin(bitwise_or)}"')
    print(f'a ^ b -> {bitwise_xor} "{bin(bitwise_xor)}"')
    print(f'   ~a -> {bitwise_not_a} "{bin(bitwise_not_a)}"')
    print(f'a << b -> {bitwise_left_shift} "{bin(bitwise_left_shift)}"')
    print(f'a >> b -> {bitwise_right_shift} "{bin(bitwise_right_shift)}"')


def _06_identity():
    x = ['apple', 'banana']
    y = ['apple', 'banana']
    z = x
    print(f'x = {x}, with address: {hex(id(x))}')
    print(f'y = {y}, with address: {hex(id(y))}')
    print(f'x = {z}, with address: {hex(id(z))}')
    print(f'x is y -> {x is y}')
    print(f'x is z -> {x is z}')
    print(f'y is z -> {y is z}')


def _07_membership():
    my_list = [1, 2, 3, 4, 5]
    print(f'my_list: {my_list}')
    print(f'3 in my_list    : {3 in my_list}')
    print(f'6 not in my_list: {6 not in my_list}')


def main():
    _01_arithmetics()
    print()

    _02_relational_comparison()
    print()

    _03_logical()
    print()

    _04_assigment()
    print()

    _05_bitwise()
    print()

    _06_identity()
    print()

    _07_membership()
    print()


if __name__ == '__main__':
    main()
