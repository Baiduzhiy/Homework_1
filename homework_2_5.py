my_list = [7, 5, 3, 3, 2]
raiting = int(input("Введите число рейтинга от 0 до 9: "))
b = len(my_list)
a = 0
for i in my_list:
    if raiting > my_list[a]:
        my_list.insert(a, raiting)
        break
    else:
        a += 1
if b == len(my_list):
    my_list.append(raiting)

print(my_list)
