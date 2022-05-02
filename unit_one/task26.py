#todo: Изучаем пакет pandas
#
# После установки библиотеки pandas выполните следующие действия:
#
# Изучите справку по модулю (для чего нужен модуль , какие возможности предоставляет)
# Найдите расположение директории модуля pandas и изучите его содержимое
# Получите список доступных атрибутов модуля pandas
# Импортируйте модуль pandas в исполняемый скрипт
# С помощью модуля pandas ознакомьтесь со структурой  DataFrame, фильтрации данных,
# загрузки данных из формата сsv (рассмотрите примеры статьи)
# Установите библиотеку matplotlib, создайте график на своем наборе данных.

#Опорная статья:  https://egorovegor.ru/pandas-obrabotka-i-analiz-dannyh-v-python/


import pandas as pd
import matplotlib.pyplot as plt

f = open("test.csv", mode="w", encoding="utf-8")
f.writelines("Месяц,Количество сделок,Доход\nянварь,100,7000000\nферваль,80,580000\nмарт,50,350000")

f.close()

df = pd.read_csv("test.csv") # Вывожу DataFrame
df.index = ["jan", "feb", "mar"]
df.index.name = "months"

Filt = {

    1: (lambda: print(df)),
    2: (lambda: print(df.loc[m])),
    3: (lambda: print(df.iloc[i])),
    4: (lambda: print(df[s1:s2])),
    5: (lambda: print(df[df["Количество сделок"] > d]["Месяц"])),
    6: (lambda: df.plot(kind='barh', y='Количество сделок', color='red') and plt.show())


}
n = 1
while True:
    n = int(input("""Введите действие:
    1: Вывести таблицу
    2: Фильтр по буквенному индексу
    3: Фильтр по числовому индексу
    4: Фильтр по срезу
    5: Фильтр по кол-ву сделок
    6: Вывод графика                                    99: Выход
    >>"""))
    if n == 99:
        print("Выход.")
        break
    if n not in range(1,7) :
        print("Ввели недопустимое значение!\n")
        continue
    if n == 2:
        m = input("Введите буквенный индекс jan/feb/mar:")
        if m not in df.index:
            print("Ошибка ввода!\n")
            continue
    if n == 3:
        i = int(input("Введите цифровой индекс от 0 до 2:"))
        if i not in range(0,3):
            print("Ошибка ввода!\n")
            continue
    if n == 4:
        s1 = int(input("Введите первое число среза:\n"))
        s2 = int(input("Введите второе число среза:\n"))
        if s1 and s2 not in [0,1,2,3]:
            print("Ошибка ввода!\n")
            continue
    if n == 5:
        d = int(input("Введите от какого кол-ва сделок смотреть таблицу:"))

    Filt[n]()



