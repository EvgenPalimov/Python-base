"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fact(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


try:
    user_answer = int(input("Введите количесто вычеслений факториала: "))
except ValueError:
    print("Вы ввели, не коректное число! Повторите ввод!")
    exit(1)

for el in fact(user_answer):
    print(el, end=' ')
