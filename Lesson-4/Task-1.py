"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

file_name, output_in_hours, hourly_rate, bonus = argv


try:
    output_in_hours = int(output_in_hours)
    hourly_rate = int(hourly_rate)
    bonus = int(bonus)
    salary = output_in_hours * hourly_rate + bonus
    print(f'Заработная плата сотрудника, состоявляет: {salary}')
except ValueError:
    print("Не правильный ввод, поторите попытку.")

