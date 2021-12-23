"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""
import random


class RandSequence:
    sequence = list
    n = int

    def __init__(self, n):
        self.n = n
        self.generate()

    def generate(self, n=None):
        if n is None:
            n = self.n
        self.sequence = [random.randint(-n, n) for _ in range(n)]

    @classmethod
    def print_seq(cls):
        print(cls.sequence)
