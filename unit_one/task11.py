# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

year = int(input("Введите год: "))
century = (year // 100) + 1
print(year, "год - ", century, "век")
