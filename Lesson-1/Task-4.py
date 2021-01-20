#Задача-4.
#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

user_number = int(input("Введите целое положтельное число: "))
max = user_number % 10

while user_number >= 10:
    user_number = user_number // 10
    if user_number % 10 > max:
        max = user_number % 10

print(f"Максимальное цифра в числе: {max}")

