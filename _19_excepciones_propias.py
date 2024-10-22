"""EXCEPCIONES PROPIAS

Podemos implementar tipos de excepciones propias extendiendo a la clase
Exception.
"""
import sys


class MyCustomException(Exception):

    def __init__(self, message: str = 'An error has occurred'):
        self.message = message
        super().__init__(self.message)


def _01_custom_exceptions():
    try:
        raise MyCustomException()
    except MyCustomException as e:
        print(e.message, file=sys.stderr)


def main():
    _01_custom_exceptions()
    print()


if __name__ == '__main__':
    main()
