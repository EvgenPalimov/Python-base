"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
"""


class MyError(Exception):
    text = "Можно вводить телько цифры!"

    def __str__(self):
        return self.text


my_list = []

while True:

    user_answer = input('Введите число, для заполения списка или наберите "stop" для выхода: ')

    if user_answer == "stop":
        break

    try:
        if not user_answer.isdigit():
            raise MyError

        my_list.append(int(user_answer))

    except MyError as err:
        print(err)

print(f"Ваш сформированый список: {my_list}")

