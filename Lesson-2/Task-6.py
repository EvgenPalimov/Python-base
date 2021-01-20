""" Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}"""

products, order = [], 1
title, price, amount, unit = None, None, None, None


while True:
    if title is None:
        tmp = input("Ввведите назание товара: ")
        if not tmp.isalnum():
            print("Наменование товара не может быть пустым. Попробуйте еще раз.")
            continue

        title = tmp

    if price is None:
        tmp = input("Введите стоимость товара: ")
        if not tmp.isdigit():
            print("Цена должна быть целым числом. Попробуйте еще раз.")
            continue

        price = tmp

    if amount is None:
        tmp = input("Введите количество: ")
        if not tmp.isdigit():
            print("Количество должно быть целым числом. Попробуйте еще раз.")
            continue

        amount = tmp

    if unit is None:
        tmp = input("Введите иденицу измерения: ")
        if not tmp.isalpha():
            print('Единица изменерения не может быть пустой. Попробуйте еще раз.')
            continue

        unit = tmp

    products.append((
        order,
        {
            'title': title,
            'price': price,
            'amount': amount,
            'unit': unit
        }
    ))

    title, price, amount, unit = None, None, None, None
    order += 1

    print('\n'.join(map(str, products)))

    q = input('Формирование списка завершено? (Да/Нет): ')
    if q.lower() == 'да':
        break

analitics = {
    'title': [],
    'price': [],
    'amount': [],
    'unit': set()
}

for _, item in products:
    analitics['title'].append(item['title'])
    analitics['price'].append(item['price'])
    analitics['amount'].append(item['amount'])
    analitics['unit'].add(item['unit'])

print(analitics)




