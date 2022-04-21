#todo: Написать функцию вычисления длины отрезка
"""Условие
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
вычисляющую расстояние между точкой (x1,y1) и (x2,y2). Ввод значений считайте функцией input()
и выведите результат работы этой функции.

Примеры входа:
0
0
1
1

выходные данные:
1.41421"""

i = 0
dots = []
while i < 4:
    dots.append(float(input("Введите координаты точек в формате x1, y1, x2, y2: ")))
    i +=1
print(dots)

def katet(x1,y1,x2,y2):
    dot_x1y1 = x1 + y1
    dot_x2y2 = x2 + y2
    result = (dot_x1y1 + dot_x2y2)**0.5
    return result
answer = katet(dots[0],dots[1],dots[2],dots[3])
print(answer)
