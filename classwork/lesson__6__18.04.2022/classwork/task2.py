# :todo Написать функцию is_ascending(list_) проверки на монотонность?
"""Функция принимает список и определяет  является ли он монотонно возрастающим
(то есть проверяет верно ли, что каждый элемент этого списка больше предыдущего).
В качестве результата возвращайте  YES, если массив монотонно возрастает и NO в противном случае.

Пример:"""

mass = [ -2, 1, 5, 7]

def is_ascending(list_):
    for i in list_:
        x = 0
        y = 1

        if list_[x:i] < list_[y:i+1]:
            print("Yes")
            x += 1
            y += 1
        else:
            print("No")
            break


result = is_ascending(mass)
print(result)



