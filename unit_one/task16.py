# todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
"""функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
чтобы каждая функция выполняла одно универсальное действие."""

words = ["Ликвидность", "Волатильность", "Спред"]
discription = ["Это возможность быстро продать актив по цене, близкой к рыночной.",
               "Это статистический финансовый показатель, характеризующий изменчивость цены на что-либо.",
               "Это разница между ценой покупки и продажи товара на рынке."]


def random_word():
    import random
    return random.randint(0, len(words) - 1)


x = random_word()

hidden_word = words[x]
hidden_discr = discription[x]
s_word = []
x_word = []
x_word_index = []
count = 0


def counter(sw):  # Если буква не встречается в списе, то счетчик +1
    if sw.count(letter) == 0:
        print("Буквы '", letter, "' нет в слове.")
        global count
        count += 1


def body(dis, xw, ):  # Основное тело, выводит описание, скрытое слово, собирает ввод, вывод кол-во баллов

    print(dis[x])
    print(xw)
    print("Количество штрафных балло", count, ".")
    letter = input("Введите букву: ")
    return letter


def finisher():  # Проверка условия кол-ва ошибок
    if count > 9:
        print("Вы набрали 10 штрафных баллов. Игра закончена.")
        return False
    else:
        return True


def winner(xw, sw):  # Прерывает цикл в случае победы
    if xw == sw:
        print("Победа!")
        print(xw)
        return False
    else:
        return True


def word_indexes(sw, lr, xwi, xw):  # индексирует отгаданные буквы и записывает в список
    for i in range(len(sw)):
        if sw[i] == lr:
            xwi.append(i)

        for i in xwi:  # подставляем вместо звездочек отгаданные буквы
            xw[i] = lr
            xwi.clear()
    return xw


def list_litter(hw, sw):  # Делаю из слова - список из его букв.
    for i in hw:
        sw.append(i)
    return sw


def list_xx(sw, xw):  # Пустой список по длине списка s_word заполняю символами ▒
    for i in range(len(sw)):
        xw.append("▒")
    return xw


list_litter(hidden_word, s_word)  # Делаю из слова - список из его букв.
list_xx(s_word, x_word)  # Пустой список по длине списка s_word заполняю символами ▒

while finisher() and winner(x_word, s_word):  # Пока баллов меньше 10 и слово полностью не разгаданно

    letter = body(discription, x_word)  # Основной тело(ввод, описание слова). Передаю в переменную введеную букву.
    counter(s_word)  # Считает штрафные баллы
    word_indexes(s_word, letter, x_word_index, x_word)  # Индекс отгаданных букв, раскрытие звездочек в слове
