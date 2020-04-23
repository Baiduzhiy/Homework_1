class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return f"Результат сложения клеток, новая клетка: {self.cells + other.cells} ячеек."

    def __sub__(self, other):
        if (self.cells - other.cells) >= 0:
            return f"Результат вычитания клеток, новая клетка: {self.cells - other.cells} ячеек."
        else:
            return f"Не возможно выполнить операцию так как у первой клетки меньше ячеек."

    def __mul__(self, other):
        return f"Результат умножения клеток, новая клетка: {self.cells * other.cells} ячеек"

    def __truediv__(self, other):
        return f"Результат деления клеток, новая клетка: {self.cells // other.cells} ячеек"

    def make_order(self):
        for i in range(self.cells // 5):
            print("* * * * *")
        print("* " * (self.cells % 5))


cell_1 = Cell(12)
print(f"Первая клетка: {cell_1.cells} ячеек.")
cell_1.make_order()
print()
cell_2 = Cell(9)
print(f"Вторая клетка: {cell_2.cells} ячеек.")
cell_2.make_order()
print()

print(cell_1 + cell_2)
new_cell = Cell(cell_1.cells + cell_2.cells)
new_cell.make_order()
print()

print(cell_1 - cell_2)
new_cell = Cell(cell_1.cells - cell_2.cells)
new_cell.make_order()
print()

print(cell_1 * cell_2)
new_cell = Cell(cell_1.cells * cell_2.cells)
new_cell.make_order()
print()

print(cell_1 / cell_2)
new_cell = Cell(int(cell_1.cells / cell_2.cells))
new_cell.make_order()


