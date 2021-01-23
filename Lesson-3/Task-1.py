"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def divided_by(*args):

    try:
        arg_1 = int(input("Введите первое число: "))
        arg_2 = int(input("Введите второе число: "))
        result = arg_1 / arg_2
    except ZeroDivisionError:
        return "На ноль, делить нельзя."

    return round(result, 2)

print(f"Итого: {divided_by()}")


"""
if arg_2 != 0:
        return arg1 / arg2
    else:
        print("На ноль, делить нельзя.")
"""