class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_division = input("Введите числа для деления (Пример - 180/20): ")

try:
    inp_division = inp_division.split("/")
    if int(inp_division[1]) == 0:
        raise OwnError("Вы ввели ноль! На ноль делить нельзя!")
    int(inp_division[0])
    int(inp_division[1])
except ValueError:
    print("Одно из значений введенное Вами не число!")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо! результат деления: {int(inp_division[0]) / int(inp_division[1])}")