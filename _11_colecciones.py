"""MÓDULO COLLECTIONS

Este módulo agrega otro tipo de colecciones que son estructuras de datos adicionales.

1. Counter
La clase Counter es empleada para contar incidencias de elementos dentro de un
iterable. Esta clase extiende de dict.

2. DefaultDict
Extiende a dict y es un diccionario que provee de un valor default a llaves
faltantes. Proporciona un valor predeterminado para los keys que no
existan. Este valor predeterminado se establece en el constructor de dicho
diccionario.

3. OrderedDict
Es un diccionario que mantiene el orden de inserción de los keys.

4. NamedTuple
Extiende de tuple y crea una nueva tupla con campos nombrados. Son como
tuplas normales, pero además de poder acceder a los campos por índices lo
podemos hacer por medio de un nombre.

5. Dequeue
Significa 'double ended queue', por lo que son colas altamente eficientes para
agregar elementos al principio o al final de la cola. Una dequeue puede funcionar
como cola o como pila. Se suelen utilizar cuando se requieren almacenar datos
de forma temporal de manera que se puedan acceder a estos eficazcmente.
"""
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque
from statistics import multimode


def _01_counter():
    some_list: list[int] = [1, 2, 5, 10, 1, 3]
    print(f'Random some_list: {some_list}')
    list_counter: Counter = Counter(some_list)
    print(f'Counter(some_list): {list_counter}')

    some_words: str = "Hello my name is Rodrigo"
    letter_counter: Counter = Counter(some_words.strip().upper())
    if ' ' in letter_counter:
        del letter_counter[' ']

    print(f'some_words: "{some_words}", and letter_counter: {letter_counter}')


def _02_default_dict():
    # default value for missing key is 0
    some_default_dict: defaultdict = defaultdict(int)
    some_default_dict['a'] = 1
    for i, c in enumerate('abcdefghijklmnopqrstuvxyz'):
        some_default_dict[c] = i + 1
    print(f'some_default_dict: {some_default_dict}')
    print(f'some_default_dict["ñ"] -> {some_default_dict["ñ"]}')

    # example 2, word counter
    frase: str = 'este es un ejemplo de una frase con algunas repetidas de ejemplo'
    conteo_palabras = defaultdict(int)
    for word in frase.strip().split():
        conteo_palabras[word] += 1
    print(f'conteo_palabras: {conteo_palabras}')


def _03_ordered_dict():
    my_dict: OrderedDict = OrderedDict()
    my_dict['a'] = 1
    my_dict['b'] = 2
    my_dict['c'] = 3
    print(f'my_dict: {my_dict}')


def _04_named_tuple():
    Person = namedtuple('Person', ['name', 'age'])
    person1 = Person('John', 25)
    person2 = Person('Wick', 45)
    print(f'person1: {person1}, person1.name = {person1.name}, person1.age = {person1.age}')
    print(f'person2: {person2}, person2.name = {person2.name}, person2.age = {person2.age}')

    Point = namedtuple('Point', ['x', 'y'])
    origin: Point = Point(1, 2)
    print(f'origin: {origin}, origin.x = {origin.x}, origin.y = {origin.y}')


def _05_dequeue():
    my_dequeue: deque = deque([1, 2, 3])
    print(f'my_dequeue: {my_dequeue}')
    for i in range(1, 10):
        if i % 2 == 0:
            my_dequeue.appendleft(i)
        else:
            my_dequeue.append(i)
    print(f'my_dequeue: {my_dequeue}')


def main():
    _01_counter()
    print()

    _02_default_dict()
    print()

    _03_ordered_dict()
    print()

    _04_named_tuple()
    print()

    _05_dequeue()
    print()


if __name__ == '__main__':
    main()
