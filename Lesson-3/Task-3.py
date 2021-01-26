"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов..
"""

def my_func(arg_1 , arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3


answer_1 = int(input("Введите первое число: "))
answer_2 = int(input("Введите второе число: "))
answer_3 = int(input("Введите третье число: "))

print(my_func(answer_1, answer_2, answer_3))

"""
Можно, стоит так записыать или лучше нет?

print(f"Результат - {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}") 
"""