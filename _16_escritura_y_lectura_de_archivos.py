"""ESCRITURA Y LECTURA DE ARCHIVOS

Python nos provee de funciones y métodos para realizar operaciones
en archivos.

1. open (read mode)
Esta función nos permite leer archivos, tomando el nombre del archivo
como primer argumento y el modo como segundo argumento.

Dentro de los modos básicos tenemos
- r (read)
- w (write)
- a (append)
- b (binary)

El objeto devuelto por open cuando el modo es de lectura, dispone de los
métodos:
- read que lee el archivo entero
- readline que lee una línea
- readiness, que lee todas las líneas del archivo regresando una lista.

2. open (write mode)
Si se emplea el modo 'w', crea un nuevo archivo. Se emplea la función
write para escribir datos en el archivo.

Notas:
- Si la función open se usa sin context manager, dicho objeto resultante
se debe cerrar llamando a close.

3. open (append mode)
Si no existe el archivo lo crea y si existe el archivo agrega al final
el nuevo contenido.
"""
import sys
from typing import AnyStr


def get_ignore_file_content() -> AnyStr:
    file_name: str = '.gitignore'
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        print(e, file=sys.stderr)


def _01_reading_file():
    file_name: str = '.gitignore'
    try:
        with open(file_name, mode='r') as f:
            content: str = f.read()
            print(content)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)


def _02_writing_file():
    file_name: str = 'gitignore_copy.txt'
    content_to_save = get_ignore_file_content()
    with open(file_name, 'w') as f:
        f.write(content_to_save)


def main():
    try:
        _01_reading_file()
        print()

        _02_writing_file()
        print()
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
