class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def numbers_at_list():
    global b
    b = []
    while True:
        numbers = input("Введите число и нажмите 'Enter' для ввода.\nДля выхода введите слово 'stop': ")
        if numbers == "stop":
            print("Процедура завершена.")
            return print(f"Список веденых чисел составил: {b}")
        try:
            if numbers.isdigit() == False:
                raise OwnError("Вы ввели не число!")
        except OwnError as err:
            print(err)
            continue
        b.append(int(numbers))


numbers_at_list()
