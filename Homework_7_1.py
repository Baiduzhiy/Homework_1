"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return '\n'.join(["".join(['%d\t' % i for i in row]) for row in self.param])

    def __add__(self, other):
        r = []
        v = 0
        for i in self.param:
            w = 0
            time_list = []
            for n in i:
                time_list.append(self.param[v][w] + other.param[v][w])
                w += 1
            r.append(time_list)
            v += 1
        return r


m = Matrix([[1, 2, 3], [3, 2, 1], [2, 3, 1]])
print(m)

print()

p = Matrix([[2, 4, 6], [3, 5, 1], [5, 5, 9]])
print(p)

print()

b = Matrix(m + p)
print(b)