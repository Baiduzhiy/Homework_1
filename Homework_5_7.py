"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

firms_info = {}

with open('text_7.txt') as my_file:
    firms = my_file.readlines()
    for i in firms:
        a = i.find(" ")
        b = i.find("/")
        firm_name = i[:a]
        firms_info[firm_name] = i[(a + 1):b].split(" ")

firms_profit = {}

for i in firms_info:
    time_profit = 0
    firms_profit[i] = int(firms_info[i][1]) - int(firms_info[i][2])

average_profit = {}

a = 1
all_sum = 0
for i in firms_profit:
    if firms_profit[i] > 0:
        all_sum += firms_profit[i]
        a += 1
    a += 1

average_profit['average_profit'] = all_sum

firms_result = firms_profit, average_profit
print(firms_result)

with open("my_file.json", "w") as write_f:
    json.dump(firms_result, write_f, ensure_ascii=False, indent=4)