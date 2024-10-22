"""TRABAJANDO CON FORMATOS DE ARCHIVOS

Podemos trabajar con diversos formatos de archivos como csv y archivos json. Python
incluye funciones para realizar conversiones, lectura y escritura en diversos formatos
de archivos.

1. csv
Empleamos el paquete csv para leer/escribir información de este tipo de archivos. Los componentes
principales de este paquete son reader, writer, DictReader y DictWriter.

2. json
Empleamos el paquete json para leer/escribir información de este tipo de archivos. Las funciones
principales son load para leer información y dump/dumps para escribir datos en archivos json.
"""
import csv
import json
import sys


def _01_cvs_read_file():
    with open('mock_data.csv', mode='r') as csv_file:
        cvs_reader = csv.reader(csv_file)
        for row in cvs_reader:
            print(row)


def _02_cvs_write_file():
    data: list = [
        ['name', 'age', 'city'],
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles'],
    ]
    with open('test_data.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)


def _03_json_read_file():
    with open('mock_data.json', mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        print(data)


def _04_json_write_file():
    data: dict = {
        'nombre': 'John Wick',
        'edad': 45,
        'email': 'john_killer@gmail.com',
    }
    try:
        with open('test_data.json', mode='w', encoding='utf-8') as f:
            json.dump(data, f)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)


def main():
    try:
        _01_cvs_read_file()
        print()

        _02_cvs_write_file()
        print()

        _03_json_read_file()
        print()

        _04_json_write_file()
        print()
    except Exception as error:
        print(error, file=sys.stderr)


if __name__ == '__main__':
    main()
