"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой..
"""

def my_func(name, surname, age, city, email, number_phone):
    return ' '.join([name, surname, age, city, email, number_phone])


print(my_func(surname='Ианов', name='Иван', age='1990', city='Екатеринбург', email='geekbrains@mail.ru',
              number_phone='8-999-999-99-99'))

"""
С запросом у пользоателя:

def my_func(**kwargs):
    name = input("Введите ваше имя: ")
    surname = input("Введите вашу фамилию: ")
    age = input("Введите ваш возраст: ")
    city = input("Введите ваш город проживания: ")
    email = input("Введите ваш e-mail: ")
    number_phone = input("Введите ваш телефон: ")
    result = ",".join([name, surname, age, city, email, number_phone])
    return result


a = my_func()
print(a)
"""