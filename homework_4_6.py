"""6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""
from itertools import count
from itertools import cycle


def counter (start, finish):
    for i in count(start):
        if i > finish:
            break
        else:
            print(i)


def cycling(text, numbers):
    c = 0
    for i in cycle(text):
        if c > numbers:
            break
        print(i)
        c += 1

counter(7, 12)
cycling("Hello", 3)


