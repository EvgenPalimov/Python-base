"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open("file_5.txt", "w") as file:
    for i in new_list:
        file.write(str(i) + " ")

with open("file_5.txt", "r") as file:
    content = file.read()
    content = content.split()
    result = sum(map(int, content))
    print(f"Сумма всех чисел:  {result}.")

