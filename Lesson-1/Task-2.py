#Задача-2.
#Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

useranswer = int(input("Введите желаемое время в секундах: "))

time_hour = useranswer // 3600
time_min = useranswer % 3600 // 60
time_sec = useranswer % 60

print(f"{useranswer} сек. составляет - {time_hour:02}:{time_min:02}:{time_sec:02}")