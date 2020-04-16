"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


workers = {}
salary = []

with open('text_3.txt') as my_file:
    for i in my_file:
        words = i.split(" ")
        del_enter = words[1]
        salary.append(del_enter[:del_enter.find("/")])
        workers[words[0]] = del_enter[:del_enter.find("/")]

for i in workers:
    if float(workers[i]) > 20000:
        print(i)

print("Имеют заработную плату более 20000.")

a = 0
for i in salary:
    a += float(i)

print(f"Средняя зарплата составляет: {a / len(salary)}")
