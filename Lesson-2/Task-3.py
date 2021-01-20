"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

sesson_list = ['Зима', 'Весна', 'Лето', 'Осень']
sesson_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}

month = int(input("Введите желаемый месяц в виде целого числа от 1 до 12: "))

if month == 12 or month == 1 or month == 2:
    print(f"По методу список: {sesson_list[0]}")
    print(f"По методу словаь: {sesson_dict.get(1)}")

elif month == 3 or month == 4 or month == 5:
    print(f"По методу список: {sesson_list[1]}")
    print(f"По методу словаь: {sesson_dict.get(2)}")

elif month == 6 or month == 7 or month == 8:
    print(f"По методу список: {sesson_list[2]}")
    print(f"По методу словаь: {sesson_dict.get(3)}")

elif month == 9 or month == 10 or month == 11:
    print(f"По методу список: {sesson_list[3]}")
    print(f"По методу словаь: {sesson_dict.get(4)}")
else:
    print("Нет такого месяца.")