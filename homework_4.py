number = int(input("Привет! Введите целое положительное число: "))
max = 0

while number != 0:
    a = number // 10
    b = number % 10
    if b == 9:
        max = b
        break
    elif b > max:
        max = b
    number = a


print(max)