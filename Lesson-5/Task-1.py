"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

new_list = []
while True:
    line = input("Введите текст: ")
    if line == "":
        break
    else:
        new_line = line + "\n"
        new_list.append(new_line)


with open('fail_1.txt', 'w', encoding="utf-8") as file:
    file.writelines(new_list)

with open("fail_1.txt", encoding="utf-8") as file:
    content = file.readlines()
    print(content)
