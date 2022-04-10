# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

a=float(input("Введите координаты точки А:"))
b=float(input("Введите координаты точки B:"))
c=float(input("Введите координаты точки C:"))
ac_lenght = abs(c-a)
bc_lenght = abs(c-b)
ac_bc_summ = ac_lenght + bc_lenght
print("Длина отрезка AC:", ac_lenght)
print("Длина отрезка BC:", bc_lenght)
print("Сумма длин отрезков AC и BC:", ac_bc_summ)