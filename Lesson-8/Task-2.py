"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text


class NegativeNumber(Exception):
    text = "Вы ввели отрицательное число!"

    def __str__(self):
        return self.text


numerator = int(input("Введите Числитель: "))
denumerator = int(input("Введите знаменатель: "))


try:
    if denumerator < 0:
        raise NegativeNumber
    if denumerator == 0:
        raise MyError
except ValueError:
    print("Вы ввели не число!")
except MyError as err:
    print(err)
except NegativeNumber as err_1:
    print(err_1)
else:
    result = numerator / denumerator
    print(f"{numerator} / {denumerator} = {result.__int__()}")






