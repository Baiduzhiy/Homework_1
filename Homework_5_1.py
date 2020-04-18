"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

my_f = open("third_try.txt", "x")
new_list = ['String_1\n', 'String_2\n', 'String_3\n', 'And next string the end\n']
my_f.writelines(new_list)
my_f.close()