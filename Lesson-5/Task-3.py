"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open("fail_3.txt", encoding="utf-8") as file:
    my_list = file.read().split('\n')
    print(my_list)
    print("_" * 50)

    staff = []
    salary = []
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            staff.append(i[0])
        salary.append(i[1])
    average_salary = sum(map(int, salary)) / len(salary)

print(f"Оклад меньше 20000 руб.,у сотрудников: {staff}, "
      f"средняя зарплата сотрудников составляет: {int(average_salary)} руб.")

