"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу..
"""

sum_result = 0
exit = False
while exit == False:
    user_answer = input('Введите числа через пробел или наберете спец. символ в любое время "q": ').split()
    result = 0
    for el in range(len(user_answer)):
        if user_answer[el] == "q":
            exit = True
            continue
        else:
            try:
                result = result + int(user_answer[el])
            except ValueError:
                print("Нужно вести целое число!")
    sum_result = sum_result + result
    print(f"Сумма ваших чисел: {result}.")
    print(f"Общая сумма всех ваших чисел: {sum_result}")
print(f"Финальная сумма всех ваших чисел: {sum_result}")