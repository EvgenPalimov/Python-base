useranswer=int(input("Введите желаемое время в секундах: "))
h=useranswer // 3600
m=useranswer // 60 % 60
s=useranswer % 60
print(f"{useranswer} сек. составляет - {h}:{m}:{s}")