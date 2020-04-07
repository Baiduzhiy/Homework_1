words = input("Введите предложение разделенные одним пробелом: ")
words_split = words.split(" ")
a = 1
for i in words_split:
    print(f"{a}-е слово:", i[0:10])
    a += 1

