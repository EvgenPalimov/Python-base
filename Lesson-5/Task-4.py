"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_list = []

with open("fail_4.1.txt", encoding="utf-8") as file:
    for i in file:
        i = i.split(" ", 1)
        new_list.append(rus[i[0]] + " " + i[1])

with open("fail_4.2.txt", "w", encoding="utf-8") as file:
    file.writelines(new_list)
