"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random


with open('numbers_to_h_5.txt', 'w+') as my_list:
    numbers = []
    for i in range(0, 20):
        a = str(random.randint(1, 100))
        numbers.append(a)
    print(numbers)
    numbers = " ".join(numbers)
    print(numbers)
    my_list.writelines(numbers)


with open('numbers_to_h_5.txt') as my_sum:
    numb = my_sum.read()
    numb = numb.split(" ")
    sum_from_txt = 0
    for i in numb:
        sum_from_txt += int(i)
    print(f" сумма всех записанных чисел в текстовый файл равна - {sum_from_txt}")

