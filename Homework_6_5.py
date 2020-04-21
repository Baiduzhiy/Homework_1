"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        pen_width = 0.5
        print(f"Запуск отрисовки. Толщина отрисовки предметом '{self.title}' составляет: {pen_width}")

class Pencil(Stationery):

    def draw(self):
        pen_width = 0.1
        print(f"Запуск отрисовки. Толщина отрисовки предметом '{self.title}' составляет: {pen_width}")

class Handle(Stationery):
    def draw(self):
        pen_width = 1.2
        print(f"Запуск отрисовки. Толщина отрисовки предметом '{self.title}' составляет: {pen_width}")

my_pen = Pen("Ручка")
my_pen.draw()

your_pen = Pencil("Карандаш")
your_pen.draw()

our_pen = Handle("Маркер")
our_pen.draw()