"""EXCEPCIONES

El manejo de excepciones en python se realiza mediante los bloques try, except, else y finally
de manera similar a java (try-catch-finally). Esto nos permite agregar seguridad ante
posibles errores que puedan suceder en tiempo de ejecución.

Dentro de try se establece el código que pueda lanzar una excepción, el bloque except se ejecuta
si ocurre una excepción mientras que else se ejecuta si no ocurre exceptión. El bloque finally
siempre se ejecutará.

Podemos lanzar una excepción de manera explícita usando la sentencia raise seguido del tipo
de excepción. Esto nos permite especificar errores concretos en situaciones concretas.

Dentro de un bloque except se pueden establecer grupos de tipos de excepciones. La sintaxis
es de la forma:
try:
    # codigo con posible error
except ExceptionType1:
    # manejo de excepción
except (ExceptionType2, ExceptionType
"""
import sys


def _01_try_except():
    try:
        print('Esto se ejecuta...')
        raise Exception('Nuevo error lanzado...')
    except Exception as e:
        print(e)
    finally:
        print(f'Esto siempre se ejecuta...')


def _02_try_except_else():
    try:
        print('Esto se ejecuta nuevamente...')
    except Exception as e:
        print(e)
    else:
        print('Se ejecuta si no hay excepción')
    finally:
        print('Siempre se ejecuta')


def _03_handling_multiple_exceptions():
    exceptions_sintaxis: str = """
    \rtry:
    \r  # possible error
    \rexcept Exception1:
    \r  # handle exception
    \rexcept Exception2:
    \r  # handle exception
    \rexcept (Exception3, Exception4):
    \r  # handle exception
    \rexcept:
    \r  # handle any other exception
    """
    print(exceptions_sintaxis)


def _04_concrete_example():
    try:
        x: int = int(input('Enter a number: '))
        result = 10 / x
        print(f'Result: {result}')
    except ValueError:
        print('Please enter a valid integer.')
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    except KeyboardInterrupt:
        print('Operation interrupted.')
    except Exception as e:
        print('An unexpected error has occurred:', e)


def main():
    _01_try_except()
    print()

    _02_try_except_else()
    print()

    _03_handling_multiple_exceptions()
    print()

    _04_concrete_example()
    print()


if __name__ == '__main__':
    main()
