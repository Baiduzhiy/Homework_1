"""6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету
и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

[int(s) for s in str.split() if s.isdigit()]
"""
lessons_dict = {}

with open('text_6.txt') as my_file:
    schedule = my_file.readlines()
    for i in schedule:
        a = i.find(":")
        key_lesson = i[:a]
        lessons_dict[key_lesson] = i[(a + 2):].split(" ")

print(lessons_dict)

for i in lessons_dict:
    lessons_hours = []
    for j in lessons_dict[i]:
        hours = "".join([s for s in j if s.isdigit()])
        lessons_hours.append(hours)
    lessons_hours = [x for x in lessons_hours if x]
    lessons_dict[i] = lessons_hours

    all_hours = 0
    for k in lessons_dict[i]:
        all_hours += int(k)

    lessons_dict[i] = all_hours

print(lessons_dict)
