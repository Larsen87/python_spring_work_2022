# todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
"""Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
Цены хранятся в словаре:"""

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}


def compute_bill(price_of_goods):
    cost = 0
    for key, val in price_of_goods.items():
        cost = cost + val
    return cost


print("Стоимость товаров равна:", compute_bill(prices))

