#Задача-3.
#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = input("Введите любое число: ")

result = int(user_number) + int(user_number * 2) + int(user_number * 3)

print(f"Сумма чисел {user_number} + {user_number * 2} + {user_number * 3} равняеться = {result}")