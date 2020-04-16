"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('text_4.txt') as my_file:
    text = my_file.readlines()

print(text)

a = 0
translate_text = []

for i in text:
    b = i.split(" ")
    words_count = 0
    for j in b:
        if j in translate:
            b[words_count] = translate[j]
        words_count += 1
    b = " ".join(b)
    translate_text.append(b)
    a += 1
print(translate_text)

with open('homework_5_4_answer.txt', 'x') as translate_file:
    translate_file.writelines(translate_text)
