"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

import re


class Date:
    def __init__(self, date: str):
        self.data = date

    @classmethod
    def Number(cls, date: str):
        nums = re.findall(r'\d+', date)
        nums = [int(i) for i in nums]
        return nums, type(nums[0])

    @staticmethod
    def Valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f"Дата указана, верна: {day}-{month}-{year} г."
                else:
                    return "Не верно указан год."
            else:
                return "Не верно указан месяц."
        else:
            return "Не верна указана дата."


print(Date.Number("01-01-2011"))

print(Date.Valid(1, 12, 2020))
print(Date.Valid(1, 13, 2020))
print(Date.Valid(32, 12, 2020))
print(Date.Valid(1, 12, 2022))
