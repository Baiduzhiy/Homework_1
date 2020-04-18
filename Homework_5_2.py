"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
number_of_strings = 0
string_len = {}
a = 1

with open('h_5_2.txt') as my_file:
    for i in my_file:
        number_of_strings += 1
    my_file.seek(0)
    for j in my_file:
        string_len[a] = len(j.split(" "))
        a += 1

print(f"Количество строк в файле {my_file.name} - {number_of_strings}")
for i in string_len:
    print(f"Количество слов в {i}-й строке - {string_len[i]}")
