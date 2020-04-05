a = int(input("Введите длину списка: "))
result_list = []
i = 0
while i < a:
    b = input("Введите значения для наполнения списков: ")
    result_list.append(b)
    i += 1
print(result_list)

change_numbers = len(result_list) - (len(result_list) % 2)
mask = 0

for i in range(0, change_numbers, 2):
    mask = result_list[i]
    result_list.pop(i)
    result_list.insert(i + 1, mask)

print("Мы немного поработали над Вашим списком и поменяли соседние значения!\nВсе они поменялись местами 1 со 2, 3 с 4, 5 с 6 и так далее...")
print(result_list)