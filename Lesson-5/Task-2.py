"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("fail_2.txt", encoding="utf-8") as file:
    print(file.read())
    print("_" * 50)
    # Не смог внести вывод текста (для вашего удобства) в первое открытия файла
    # Когда вносил, почему-то цикл for не выполнялся, так и не понял почему.
    # Видимо "read" закрывет его, мое предположение.
with open("fail_2.txt", encoding="utf-8") as file:
    lines = 0
    litters = 0
    for line in file:
        lines += 1
        litters = len(line.split())
        print(f"{litters} слов(о) в {i} строке.")
print(f"Количество строк в файле: {lines} строки.")
