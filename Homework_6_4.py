"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.__is_police = is_police

    def go(self):
        print(f"Автомобиль поехал")

    def stop(self):
        print(f"Автомобиль остановился")

    def turn(self, direction):
        print(f"Автомобиль повернул на {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Вы превысили скорость!")
        else:
            print(f"Скорость автомобиля {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Вы превысили скорость!")
        else:
            print(f"Скорость автомобиля {self.speed}")


class PoliceCar(Car):
    pass


lexus = TownCar(70, "Black", "Lexus")

lexus.go()
lexus.turn("право")
lexus.turn("лево")
lexus.show_speed()
lexus.stop()
