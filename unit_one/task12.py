#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
#>4

#Введите  массу тела
#>1

#Ответ: 1000 кг

ed_mass = input("""Введите единицу массы тела:
        1 - килограмм
        2 — миллиграмм
        3 — грамм
        4 — тонна
        5 — центнер 
        """)
weight = (float(input("Введите массу тела: ")))

match ed_mass:
    case "1":
        print("Ответ: ",weight,"килограмм")
    case "2":
        print("Ответ: ",weight,"миллиграмм")
    case "3":
        print("Ответ: ",weight,"грамм")
    case "4":
        print("Ответ: ",weight,"тонна")
    case "5":
        print("Ответ: ",weight,"центнер")
